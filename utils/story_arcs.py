"""Story arc templates and structures for age-appropriate storytelling."""

from typing import Dict, List


class StoryArc:
    """Template for story structure appropriate for ages 5-10."""
    
    THREE_ACT_STRUCTURE = {
        "act_1": {
            "name": "Beginning",
            "description": "Introduce characters and setting. Show the normal world and what the main character wants.",
            "percentage": 25,
            "elements": [
                "Who is the main character?",
                "Where does the story take place?",
                "What does the character want or need?",
                "What is their everyday life like?"
            ]
        },
        "act_2": {
            "name": "Middle",
            "description": "The character faces challenges and tries to solve problems. Things get complicated.",
            "percentage": 50,
            "elements": [
                "What problem or challenge does the character face?",
                "How do they try to solve it?",
                "What obstacles get in their way?",
                "What happens when they try different solutions?"
            ]
        },
        "act_3": {
            "name": "Ending",
            "description": "The problem is solved, and the character learns something or grows.",
            "percentage": 25,
            "elements": [
                "How is the problem finally solved?",
                "What did the character learn?",
                "How are things different now?",
                "What is the happy ending or resolution?"
            ]
        }
    }
    
    FIVE_PART_STRUCTURE = {
        "exposition": {
            "name": "Introduction",
            "description": "Meet the characters and learn about their world",
            "percentage": 20
        },
        "rising_action": {
            "name": "The Problem",
            "description": "Something happens that creates a challenge",
            "percentage": 25
        },
        "climax": {
            "name": "The Big Moment",
            "description": "The most exciting part where the character faces the biggest challenge",
            "percentage": 20
        },
        "falling_action": {
            "name": "Working It Out",
            "description": "The character solves the problem",
            "percentage": 20
        },
        "resolution": {
            "name": "Happy Ending",
            "description": "Everything is resolved and the character is happy",
            "percentage": 15
        }
    }
    
    @staticmethod
    def get_arc_template(arc_type: str = "three_act") -> Dict:
        """
        Get a story arc template.
        
        Args:
            arc_type: Either "three_act" or "five_part"
            
        Returns:
            Dictionary containing the story arc structure
        """
        if arc_type == "three_act":
            return StoryArc.THREE_ACT_STRUCTURE
        elif arc_type == "five_part":
            return StoryArc.FIVE_PART_STRUCTURE
        else:
            raise ValueError(f"Unknown arc type: {arc_type}. Use 'three_act' or 'five_part'.")
    
    @staticmethod
    def format_arc_guidance(arc_type: str = "three_act") -> str:
        """
        Format story arc guidance as a prompt-friendly string.
        
        Args:
            arc_type: Either "three_act" or "five_part"
            
        Returns:
            Formatted string with arc guidance
        """
        template = StoryArc.get_arc_template(arc_type)
        
        guidance = f"Use a {arc_type.replace('_', '-')} story structure:\n\n"
        
        for key, value in template.items():
            guidance += f"{value['name']} ({value['percentage']}% of story):\n"
            guidance += f"{value['description']}\n"
            if 'elements' in value:
                guidance += "Key elements to include:\n"
                for element in value['elements']:
                    guidance += f"- {element}\n"
            guidance += "\n"
        
        return guidance


# Age-appropriate guidelines
AGE_GUIDELINES = {
    "vocabulary": {
        "recommended": "Use simple, clear words. Avoid complex vocabulary unless necessary, and explain new words in context.",
        "avoid": "Jargon, overly technical terms, or words that require advanced reading comprehension"
    },
    "sentence_length": {
        "recommended": "Mix short and medium sentences. Keep most sentences under 15-20 words.",
        "avoid": "Very long, complex sentences with multiple clauses"
    },
    "themes": {
        "recommended": [
            "Friendship and helping others",
            "Being brave and trying new things",
            "Solving problems creatively",
            "Learning from mistakes",
            "Kindness and empathy",
            "Working together",
            "Being yourself"
        ],
        "avoid": [
            "Scary or frightening content",
            "Violence or conflict without resolution",
            "Complex emotional themes beyond a child's understanding",
            "Negative stereotypes",
            "Inappropriate or mature content"
        ]
    },
    "story_length": {
        "recommended": "500-1000 words for a complete bedtime story",
        "paragraphs": "3-5 paragraphs per section, keeping each paragraph focused on one idea"
    }
}


def get_age_guidelines() -> str:
    """
    Get age-appropriateness guidelines formatted for prompts.
    
    Returns:
        Formatted string with age guidelines
    """
    guidelines = "AGE-APPROPRIATENESS GUIDELINES (Ages 5-10):\n\n"
    
    guidelines += "VOCABULARY:\n"
    guidelines += f"- Recommended: {AGE_GUIDELINES['vocabulary']['recommended']}\n"
    guidelines += f"- Avoid: {AGE_GUIDELINES['vocabulary']['avoid']}\n\n"
    
    guidelines += "SENTENCE STRUCTURE:\n"
    guidelines += f"- Recommended: {AGE_GUIDELINES['sentence_length']['recommended']}\n"
    guidelines += f"- Avoid: {AGE_GUIDELINES['sentence_length']['avoid']}\n\n"
    
    guidelines += "APPROPRIATE THEMES:\n"
    for theme in AGE_GUIDELINES['themes']['recommended']:
        guidelines += f"- {theme}\n"
    
    guidelines += "\nTHEMES TO AVOID:\n"
    for theme in AGE_GUIDELINES['themes']['avoid']:
        guidelines += f"- {theme}\n"
    
    guidelines += f"\nSTORY LENGTH:\n"
    guidelines += f"- Target: {AGE_GUIDELINES['story_length']['recommended']}\n"
    guidelines += f"- Structure: {AGE_GUIDELINES['story_length']['paragraphs']}\n"
    
    return guidelines

