"""Judge agent that evaluates story quality and provides feedback."""

from typing import Dict, List, Optional
from agents.base_agent import BaseAgent
from prompts.prompt_templates import PromptTemplate
from utils.story_arcs import get_age_guidelines


class JudgeAgent(BaseAgent):
    """Agent that evaluates stories on multiple dimensions and provides feedback."""
    
    EVALUATION_DIMENSIONS = [
        "Age-appropriateness",
        "Narrative coherence",
        "Character development",
        "Engagement level",
        "Educational/moral value"
    ]
    
    def __init__(self, model: str = "gpt-3.5-turbo"):
        """Initialize the judge agent."""
        super().__init__(model)
        self.temperature = 0.2  # Low temperature for consistent, reasoned evaluations
    
    def evaluate_story(self, story: str) -> Dict:
        """
        Evaluate a story on multiple dimensions.
        
        Args:
            story: The story text to evaluate
            
        Returns:
            Dictionary containing scores, reasoning, and suggestions for each dimension
        """
        prompt_base = PromptTemplate.create_evaluation_prompt_base()
        prompt = PromptTemplate.format_prompt(
            prompt_base,
            variables={
                "guidelines": get_age_guidelines(),
                "story": story
            }
        )
        
        response = self.call_model(
            prompt=prompt,
            max_tokens=1500,
            temperature=self.temperature
        )
        
        # Parse the structured response
        evaluation = self._parse_evaluation(response, story)
        
        return evaluation
    
    def _parse_evaluation(self, response: str, story: str) -> Dict:
        """
        Parse the judge's evaluation response into structured data.
        
        Args:
            response: Raw evaluation response from the LLM
            story: The original story text
            
        Returns:
            Dictionary with structured evaluation data
        """
        evaluation = {
            "dimensions": {},
            "overall_score": 0.0,
            "overall_assessment": "",
            "key_improvements": [],
            "raw_response": response
        }
        
        lines = response.split("\n")
        current_dimension = None
        current_section = None
        
        for line in lines:
            line = line.strip()
            
            # Check for dimension headers
            if line.upper().startswith("DIMENSION:"):
                current_dimension = line.replace("DIMENSION:", "").strip()
                evaluation["dimensions"][current_dimension] = {
                    "score": None,
                    "reasoning": "",
                    "suggestions": []
                }
                current_section = None
                continue
            
            # Check for score
            if line.upper().startswith("SCORE:"):
                score_text = line.replace("SCORE:", "").strip()
                # Extract numeric score (e.g., "8/10" -> 8)
                try:
                    score = float(score_text.split("/")[0].strip())
                    if current_dimension:
                        evaluation["dimensions"][current_dimension]["score"] = score
                except (ValueError, IndexError):
                    pass
                current_section = "score"
                continue
            
            # Check for reasoning
            if line.upper().startswith("REASONING:"):
                current_section = "reasoning"
                if current_dimension:
                    reasoning = line.replace("REASONING:", "").strip()
                    evaluation["dimensions"][current_dimension]["reasoning"] = reasoning
                continue
            
            # Check for suggestions
            if line.upper().startswith("SUGGESTIONS:"):
                current_section = "suggestions"
                if current_dimension:
                    suggestion = line.replace("SUGGESTIONS:", "").strip()
                    if suggestion and suggestion.lower() != "no major improvements needed":
                        evaluation["dimensions"][current_dimension]["suggestions"].append(suggestion)
                continue
            
            # Check for overall assessment
            if line.upper().startswith("OVERALL_ASSESSMENT") or line.upper().startswith("OVERALL ASSESSMENT"):
                current_section = "overall"
                continue
            
            # Check for key improvements
            if line.upper().startswith("SUMMARY_OF_KEY_IMPROVEMENTS") or line.upper().startswith("KEY IMPROVEMENTS"):
                current_section = "improvements"
                continue
            
            # Append content to current section
            if current_section and line:
                if current_section == "reasoning" and current_dimension:
                    if evaluation["dimensions"][current_dimension]["reasoning"]:
                        evaluation["dimensions"][current_dimension]["reasoning"] += " " + line
                    else:
                        evaluation["dimensions"][current_dimension]["reasoning"] = line
                elif current_section == "suggestions" and current_dimension:
                    if line and not line.lower().startswith("no major"):
                        evaluation["dimensions"][current_dimension]["suggestions"].append(line)
                elif current_section == "overall":
                    evaluation["overall_assessment"] += line + " "
                elif current_section == "improvements":
                    if line:
                        evaluation["key_improvements"].append(line)
        
        # Calculate overall score as average of dimension scores
        scores = []
        for dim_name, dim_data in evaluation["dimensions"].items():
            if dim_data["score"] is not None:
                scores.append(dim_data["score"])
        
        if scores:
            evaluation["overall_score"] = sum(scores) / len(scores)
        
        # Clean up text fields
        evaluation["overall_assessment"] = evaluation["overall_assessment"].strip()
        
        return evaluation
    
    def should_refine(self, evaluation: Dict, threshold: float = 7.0) -> bool:
        """
        Determine if a story should be refined based on evaluation scores.
        
        Args:
            evaluation: The evaluation dictionary
            threshold: Minimum average score to avoid refinement
            
        Returns:
            True if story should be refined, False otherwise
        """
        if evaluation["overall_score"] < threshold:
            return True
        
        # Also check if any dimension is below threshold
        for dim_name, dim_data in evaluation["dimensions"].items():
            if dim_data["score"] is not None and dim_data["score"] < threshold:
                return True
        
        return False
    
    def get_refinement_instructions(self, evaluation: Dict) -> str:
        """
        Generate instructions for refining a story based on evaluation.
        
        Args:
            evaluation: The evaluation dictionary
            
        Returns:
            Formatted string with refinement instructions
        """
        instructions = "Based on the evaluation, please improve the story by addressing the following:\n\n"
        
        for dim_name, dim_data in evaluation["dimensions"].items():
            if dim_data["score"] is not None and dim_data["score"] < 8.0:
                instructions += f"{dim_name} (Score: {dim_data['score']}/10):\n"
                if dim_data["reasoning"]:
                    instructions += f"Reasoning: {dim_data['reasoning']}\n"
                if dim_data["suggestions"]:
                    instructions += "Suggestions:\n"
                    for suggestion in dim_data["suggestions"]:
                        instructions += f"- {suggestion}\n"
                instructions += "\n"
        
        if evaluation["key_improvements"]:
            instructions += "Key Improvements:\n"
            for improvement in evaluation["key_improvements"]:
                instructions += f"- {improvement}\n"
        
        return instructions

