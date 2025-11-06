"""Prompt template utilities and formatting functions."""

from typing import Dict, List, Optional
from utils.story_arcs import StoryArc, get_age_guidelines


class PromptTemplate:
    """Utility class for creating and formatting prompts."""
    
    @staticmethod
    def format_prompt(
        base_prompt: str,
        variables: Optional[Dict[str, str]] = None,
        examples: Optional[List[str]] = None,
        additional_guidelines: Optional[str] = None
    ) -> str:
        """
        Format a prompt template with variables and optional components.
        
        Args:
            base_prompt: The base prompt template
            variables: Dictionary of variables to replace in the template
            examples: List of example strings to include
            additional_guidelines: Additional guidelines to append
            
        Returns:
            Formatted prompt string
        """
        prompt = base_prompt
        
        # Replace variables
        if variables:
            for key, value in variables.items():
                prompt = prompt.replace(f"{{{key}}}", str(value))
        
        # Add examples if provided
        if examples:
            prompt += "\n\nEXAMPLES:\n"
            for i, example in enumerate(examples, 1):
                prompt += f"\nExample {i}:\n{example}\n"
        
        # Add additional guidelines
        if additional_guidelines:
            prompt += f"\n\nADDITIONAL GUIDELINES:\n{additional_guidelines}"
        
        return prompt
    
    @staticmethod
    def create_story_prompt_base() -> str:
        """Create the base prompt structure for story generation."""
        return (
            "You are a talented children's storyteller who creates engaging, "
            "age-appropriate bedtime stories for children ages 5-10.\n\n"
            "{guidelines}"
            "\n\nSTORY REQUEST:\n{user_request}\n\n"
            "Please create a complete bedtime story based on this request. "
            "The story should be engaging, have clear characters, and follow "
            "a satisfying story arc with a beginning, middle, and end."
        )
    
    @staticmethod
    def create_evaluation_prompt_base() -> str:
        """Create the base prompt structure for story evaluation."""
        return (
            "You are an expert evaluator of children's stories (ages 5-10). "
            "Evaluate the following story and provide detailed feedback.\n\n"
            "{guidelines}"
            "\n\nSTORY TO EVALUATE:\n{story}\n\n"
            "Please evaluate this story on the following dimensions:\n"
            "1. Age-appropriateness (1-10)\n"
            "2. Narrative coherence (1-10)\n"
            "3. Character development (1-10)\n"
            "4. Engagement level (1-10)\n"
            "5. Educational/moral value (1-10)\n\n"
            "For each dimension, provide:\n"
            "- A numerical score (1-10)\n"
            "- Brief reasoning for your score\n"
            "- Specific, actionable suggestions for improvement (if score < 8)\n\n"
            "Format your response as follows:\n"
            "DIMENSION: [Name]\n"
            "SCORE: [X/10]\n"
            "REASONING: [Brief explanation]\n"
            "SUGGESTIONS: [Specific improvements, or 'No major improvements needed' if score >= 8]\n\n"
            "After all dimensions, provide an OVERALL_ASSESSMENT and "
            "SUMMARY_OF_KEY_IMPROVEMENTS (if any)."
        )
    
    @staticmethod
    def create_categorization_prompt_base() -> str:
        """Create the base prompt structure for story categorization."""
        return (
            "You are a story classifier. Analyze the following story request "
            "and categorize it into one of these types:\n\n"
            "CATEGORIES:\n"
            "1. ADVENTURE - Stories about journeys, quests, exploration, discovery\n"
            "2. FRIENDSHIP - Stories about relationships, helping friends, teamwork\n"
            "3. MAGIC/FANTASY - Stories with magical elements, fantasy creatures, wonder\n"
            "4. ANIMALS - Stories featuring animals as main characters\n"
            "5. PROBLEM-SOLVING - Stories about overcoming challenges, puzzles, creativity\n"
            "6. EVERYDAY - Stories about normal life situations, school, family\n"
            "7. MIXED - Stories that combine multiple categories\n\n"
            "STORY REQUEST:\n{user_request}\n\n"
            "Respond with ONLY the category name (e.g., 'ADVENTURE' or 'FRIENDSHIP') "
            "followed by a brief explanation (1-2 sentences) of why you chose this category."
        )

