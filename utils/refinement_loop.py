"""Refinement loop that connects storyteller and judge for iterative improvement."""

from typing import Dict, Optional
from agents.storyteller import StorytellerAgent
from agents.judge import JudgeAgent
from prompts.prompt_templates import PromptTemplate
from utils.story_arcs import get_age_guidelines


class RefinementLoop:
    """Manages the iterative refinement process between storyteller and judge."""
    
    def __init__(
        self,
        storyteller: Optional[StorytellerAgent] = None,
        judge: Optional[JudgeAgent] = None,
        max_iterations: int = 2
    ):
        """
        Initialize the refinement loop.
        
        Args:
            storyteller: Storyteller agent instance (creates new if None)
            judge: Judge agent instance (creates new if None)
            max_iterations: Maximum number of refinement iterations
        """
        self.storyteller = storyteller or StorytellerAgent()
        self.judge = judge or JudgeAgent()
        self.max_iterations = max_iterations
    
    def refine_story(
        self,
        original_story: str,
        user_request: str,
        category: str,
        threshold: float = 7.0
    ) -> Dict:
        """
        Refine a story iteratively based on judge feedback.
        
        Args:
            original_story: The initial story
            user_request: Original user request
            category: Story category
            threshold: Minimum score threshold to stop refinement
            
        Returns:
            Dictionary with final story, evaluation, and iteration info
        """
        current_story = original_story
        iteration = 0
        all_evaluations = []
        
        while iteration < self.max_iterations:
            iteration += 1
            
            # Evaluate the current story
            evaluation = self.judge.evaluate_story(current_story)
            all_evaluations.append({
                "iteration": iteration,
                "evaluation": evaluation,
                "story": current_story
            })
            
            # Check if we should continue refining
            if not self.judge.should_refine(evaluation, threshold):
                break
            
            # Get refinement instructions
            refinement_instructions = self.judge.get_refinement_instructions(evaluation)
            
            # Generate improved story
            improved_story = self._generate_refined_story(
                current_story=current_story,
                user_request=user_request,
                category=category,
                refinement_instructions=refinement_instructions
            )
            
            current_story = improved_story
        
        return {
            "final_story": current_story,
            "final_evaluation": all_evaluations[-1]["evaluation"],
            "iterations": iteration,
            "all_evaluations": all_evaluations,
            "improved": iteration > 1
        }
    
    def _generate_refined_story(
        self,
        current_story: str,
        user_request: str,
        category: str,
        refinement_instructions: str
    ) -> str:
        """
        Generate a refined version of the story based on feedback.
        
        Args:
            current_story: The current story version
            user_request: Original user request
            category: Story category
            refinement_instructions: Instructions for improvement
            
        Returns:
            Improved story text
        """
        prompt = (
            "You are a talented children's storyteller improving a bedtime story "
            "based on expert feedback.\n\n"
            f"{get_age_guidelines()}\n\n"
            "ORIGINAL STORY REQUEST:\n"
            f"{user_request}\n\n"
            "CURRENT STORY:\n"
            f"{current_story}\n\n"
            "FEEDBACK FOR IMPROVEMENT:\n"
            f"{refinement_instructions}\n\n"
            f"STORY CATEGORY: {category}\n\n"
            "Please create an improved version of the story that addresses the feedback "
            "while maintaining the core story elements and ensuring it remains appropriate "
            "for children ages 5-10. The story should be complete and engaging."
        )
        
        improved_story = self.storyteller.call_model(
            prompt=prompt,
            max_tokens=2000,
            temperature=0.7  # Slightly lower temperature for refinement
        )
        
        return improved_story.strip()

