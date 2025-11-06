"""
Main entry point for the storytelling system.

This system uses multiple agents (categorizer, storyteller, judge) to create
high-quality, age-appropriate bedtime stories for children ages 5-10.
"""

from typing import Dict
from agents.categorizer import CategorizerAgent
from agents.storyteller import StorytellerAgent
from agents.judge import JudgeAgent
from utils.refinement_loop import RefinementLoop

"""
Before submitting the assignment, describe here in a few sentences what you would have built next if you spent 2 more hours on this project:

If I had 2 more hours, I would focus on:
1. **Multi-judge ensemble**: Implement a system where multiple judge evaluations are averaged for more reliable scoring and to reduce variance in quality assessment.
2. **Story persistence and learning**: Add a system to store successful stories and their evaluations, allowing the system to learn from past examples and improve few-shot selection dynamically.
3. **User preference learning**: Track which stories users like most and adapt generation parameters (temperature, story arc type, category weights) based on user feedback patterns.
4. **Enhanced visualization**: Create a visual story arc diagram showing the progression of the story, and a dashboard showing evaluation scores over time to help users understand story quality metrics.
5. **Story customization options**: Allow users to specify story length, preferred themes, or specific characters before generation, making the system more interactive and user-controlled.
"""


class StorytellingSystem:
    """Main orchestration class for the storytelling system."""
    
    def __init__(self):
        """Initialize all agents."""
        self.categorizer = CategorizerAgent()
        self.storyteller = StorytellerAgent()
        self.judge = JudgeAgent()
        self.refinement_loop = RefinementLoop(
            storyteller=self.storyteller,
            judge=self.judge,
            max_iterations=2
        )
    
    def create_story(
        self,
        user_request: str,
        enable_refinement: bool = True,
        show_details: bool = False
    ) -> Dict:
        """
        Create a story from user request through the full pipeline.
        
        Args:
            user_request: The user's story request
            enable_refinement: Whether to use judge refinement loop
            show_details: Whether to show intermediate steps
            
        Returns:
            Dictionary with story, category, and evaluation info
        """
        if show_details:
            print("\n" + "=" * 60)
            print("Storytelling System Pipeline")
            print("=" * 60)
        
        # Step 1: Categorize the request
        if show_details:
            print("\n[Step 1] Categorizing story request...")
        category, explanation = self.categorizer.categorize(user_request)
        if show_details:
            print(f"Category: {category}")
            print(f"Explanation: {explanation}")
        
        # Step 2: Generate initial story
        if show_details:
            print(f"\n[Step 2] Generating {category.lower()} story...")
        initial_story = self.storyteller.generate_story(
            user_request=user_request,
            category=category,
            use_story_arc=True,
            arc_type="three_act"
        )
        if show_details:
            print(f"Initial story generated ({len(initial_story)} characters)")
        
        # Step 3: Evaluate and refine (if enabled)
        final_story = initial_story
        evaluation = None
        refined = False
        
        if enable_refinement:
            if show_details:
                print("\n[Step 3] Evaluating and refining story...")
            
            result = self.refinement_loop.refine_story(
                original_story=initial_story,
                user_request=user_request,
                category=category,
                threshold=7.0
            )
            
            final_story = result["final_story"]
            evaluation = result["final_evaluation"]
            refined = result["improved"]
            
            if show_details:
                print(f"Refinement iterations: {result['iterations']}")
                if refined:
                    print("Story was refined based on judge feedback")
                else:
                    print("Story met quality threshold, no refinement needed")
        
        return {
            "story": final_story,
            "category": category,
            "category_explanation": explanation,
            "evaluation": evaluation,
            "refined": refined,
            "initial_story": initial_story if enable_refinement else None
        }


def main():
    """
    Main entry point for the storytelling application.
    """
    print("=" * 60)
    print("Welcome to the Storytelling System!")
    print("Creating age-appropriate bedtime stories for children ages 5-10")
    print("=" * 60)
    
    try:
        system = StorytellingSystem()
        
        # Get user input
        user_request = input("\nWhat kind of story do you want to hear? ")
        
        if not user_request.strip():
            print("Using example story request...")
            user_request = "A story about a girl named Alice and her best friend Bob, who happens to be a cat."
        
        print("\n" + "=" * 60)
        print("Generating your story...")
        print("=" * 60)
        
        # Create the story
        result = system.create_story(
            user_request=user_request,
            enable_refinement=True,
            show_details=True
        )
        
        # Display results
        print("\n" + "=" * 60)
        print("Your Story")
        print("=" * 60)
        print(f"\nCategory: {result['category']}")
        print(f"Explanation: {result['category_explanation']}\n")
        
        print("-" * 60)
        print(result['story'])
        print("-" * 60)
        
        # Show evaluation if available
        if result['evaluation']:
            print("\n" + "=" * 60)
            print("Story Quality Evaluation")
            print("=" * 60)
            eval_data = result['evaluation']
            print(f"\nOverall Score: {eval_data['overall_score']:.1f}/10")
            
            if eval_data['overall_assessment']:
                print(f"\nAssessment: {eval_data['overall_assessment']}")
            
            print("\nDimension Scores:")
            for dim_name, dim_data in eval_data['dimensions'].items():
                score = dim_data['score'] if dim_data['score'] is not None else "N/A"
                print(f"  - {dim_name}: {score}/10")
        
        # Ask for user feedback
        print("\n" + "=" * 60)
        feedback = input("Would you like to request any changes to the story? (yes/no): ").strip().lower()
        
        if feedback in ['yes', 'y']:
            modification = input("What would you like to change? ")
            if modification.strip():
                print("\nGenerating modified story...")
                modified_result = system.create_story(
                    user_request=f"{user_request} {modification}",
                    enable_refinement=True,
                    show_details=False
                )
                print("\n" + "=" * 60)
                print("Modified Story")
                print("=" * 60)
                print(modified_result['story'])
        
        print("\n" + "=" * 60)
        print("Thank you for using the Storytelling System!")
        print("=" * 60)
        
    except ValueError as e:
        print(f"\nError: {e}")
        print("Please make sure you have set OPENAI_API_KEY in your .env file")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()