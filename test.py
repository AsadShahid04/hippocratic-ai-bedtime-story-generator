"""
Test file for the storytelling system infrastructure.
Run this to test components as we build them.
"""

from agents.base_agent import BaseAgent
from utils.story_arcs import StoryArc, get_age_guidelines
from prompts.prompt_templates import PromptTemplate


def test_infrastructure():
    """Test the infrastructure components that don't require API calls."""
    print("=" * 60)
    print("Testing Infrastructure Components")
    print("=" * 60)
    
    # Test 1: Story Arc Templates
    print("\n[TEST 1] Story Arc Templates")
    print("-" * 60)
    three_act = StoryArc.format_arc_guidance("three_act")
    print("Three-Act Structure (first 200 chars):")
    print(three_act[:200] + "...")
    print("✓ Story arc templates working")
    
    five_part = StoryArc.format_arc_guidance("five_part")
    print("\nFive-Part Structure exists:")
    print(f"✓ {len(five_part)} characters of guidance generated")
    
    # Test 2: Age Guidelines
    print("\n[TEST 2] Age-Appropriateness Guidelines")
    print("-" * 60)
    guidelines = get_age_guidelines()
    print("Guidelines preview (first 300 chars):")
    print(guidelines[:300] + "...")
    print(f"✓ Age guidelines generated ({len(guidelines)} chars)")
    
    # Test 3: Prompt Template Formatting
    print("\n[TEST 3] Prompt Template Formatting")
    print("-" * 60)
    base_prompt = PromptTemplate.create_story_prompt_base()
    formatted = PromptTemplate.format_prompt(
        base_prompt,
        variables={
            "guidelines": get_age_guidelines(),
            "user_request": "A story about a brave little bunny"
        },
        additional_guidelines=StoryArc.format_arc_guidance("three_act")
    )
    print("Formatted prompt preview (first 400 chars):")
    print(formatted[:400] + "...")
    print(f"✓ Prompt templates working ({len(formatted)} chars total)")
    
    # Test 4: Categorization Prompt
    print("\n[TEST 4] Categorization Prompt Template")
    print("-" * 60)
    cat_prompt = PromptTemplate.create_categorization_prompt_base()
    cat_formatted = PromptTemplate.format_prompt(
        cat_prompt,
        variables={"user_request": "A story about a girl named Alice and her best friend Bob, who happens to be a cat."}
    )
    print("Categorization prompt preview (first 300 chars):")
    print(cat_formatted[:300] + "...")
    print("✓ Categorization prompts working")
    
    # Test 5: Evaluation Prompt
    print("\n[TEST 5] Evaluation Prompt Template")
    print("-" * 60)
    eval_prompt = PromptTemplate.create_evaluation_prompt_base()
    eval_formatted = PromptTemplate.format_prompt(
        eval_prompt,
        variables={
            "guidelines": get_age_guidelines(),
            "story": "Once upon a time, there was a brave bunny..."
        }
    )
    print("Evaluation prompt preview (first 300 chars):")
    print(eval_formatted[:300] + "...")
    print("✓ Evaluation prompts working")
    
    print("\n" + "=" * 60)
    print("All infrastructure tests passed! ✓")
    print("=" * 60)


def test_api_connection():
    """Test that the API key is set up correctly."""
    print("\n" + "=" * 60)
    print("Testing API Connection")
    print("=" * 60)
    
    try:
        agent = BaseAgent()
        print("✓ BaseAgent initialized successfully")
        print("✓ OpenAI API key loaded from .env file")
        print("\nNote: This doesn't make an actual API call yet.")
        print("The agents will be implemented in Phase 2.")
        return True
    except ValueError as e:
        print(f"\n✗ Error: {e}")
        print("\nTo test API connection:")
        print("1. Open the .env file")
        print("2. Replace 'your_openai_api_key_here' with your actual OpenAI API key")
        print("3. Run this script again")
        return False


def test_story_arc_retrieval():
    """Test retrieving story arc templates."""
    print("\n" + "=" * 60)
    print("Testing Story Arc Retrieval")
    print("=" * 60)
    
    try:
        three_act = StoryArc.get_arc_template("three_act")
        print(f"✓ Three-act structure has {len(three_act)} acts")
        for act_name, act_data in three_act.items():
            print(f"  - {act_data['name']}: {act_data['percentage']}%")
        
        five_part = StoryArc.get_arc_template("five_part")
        print(f"\n✓ Five-part structure has {len(five_part)} parts")
        for part_name, part_data in five_part.items():
            print(f"  - {part_data['name']}: {part_data['percentage']}%")
        
        # Test error handling
        try:
            StoryArc.get_arc_template("invalid")
            print("✗ Should have raised ValueError")
        except ValueError:
            print("✓ Error handling works correctly")
        
    except Exception as e:
        print(f"✗ Error: {e}")


def main():
    """Run all tests."""
    print("=" * 60)
    print("Storytelling System - Test Suite")
    print("Phase 1: Core Infrastructure Testing")
    print("=" * 60)
    
    # Test infrastructure (no API calls needed)
    test_infrastructure()
    
    # Test story arc retrieval
    test_story_arc_retrieval()
    
    # Test API connection (requires .env to be set)
    api_connected = test_api_connection()
    
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    print("✓ Infrastructure components tested")
    print("✓ Story arc templates tested")
    if api_connected:
        print("✓ API connection ready")
    else:
        print("⚠ API key not set (not required for infrastructure tests)")
    
    print("\nNext Steps:")
    print("1. Add your OpenAI API key to .env file (if not done)")
    print("2. Proceed with Phase 2: Agent Implementation")
    print("=" * 60)


if __name__ == "__main__":
    main()

