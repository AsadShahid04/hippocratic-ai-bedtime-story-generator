"""Storyteller agent that generates age-appropriate bedtime stories."""

from typing import Optional, Dict
from agents.base_agent import BaseAgent
from prompts.prompt_templates import PromptTemplate
from utils.story_arcs import StoryArc, get_age_guidelines


class StorytellerAgent(BaseAgent):
    """Agent that generates engaging bedtime stories for children ages 5-10."""
    
    # Category-specific story examples (few-shot learning)
    CATEGORY_EXAMPLES = {
        "ADVENTURE": """Example Adventure Story (excerpt):
Once upon a time, there was a brave little explorer named Maya who loved discovering new places. One sunny morning, Maya found a mysterious map in her grandmother's attic. The map showed a path to a hidden treasure in the nearby forest.

Maya grabbed her backpack filled with snacks and a flashlight, and set off on her adventure. She followed the map carefully, crossing streams and climbing small hills. Along the way, she met friendly animals who helped her find the right path.

Finally, after solving a tricky puzzle written on an old tree, Maya discovered the treasure: a beautiful collection of her grandmother's childhood memories. The real treasure was learning about her family's history and the joy of exploring.""",

        "FRIENDSHIP": """Example Friendship Story (excerpt):
Lily and Sam were best friends who did everything together. One day, a new student named Alex joined their class. Alex seemed shy and didn't talk to anyone.

Lily noticed Alex sitting alone during lunch and decided to invite them to join her and Sam. At first, Sam felt a little left out because Lily was spending time with Alex. But then Sam realized that having more friends meant more fun!

Together, the three friends discovered they all loved the same games and stories. They learned that friendship isn't about having just one friend, but about making room for everyone. Lily, Sam, and Alex became the best of friends, and they always included each other in their adventures.""",

        "MAGIC/FANTASY": """Example Magic/Fantasy Story (excerpt):
In a small town where magic was hidden in everyday things, lived a young girl named Emma who could talk to flowers. Every morning, the flowers in her garden would whisper stories about the magical creatures that lived in the nearby woods.

One evening, a tiny fairy named Pip appeared at Emma's window, asking for help. The fairy's magical forest was losing its sparkle because the creatures had forgotten how to believe in magic.

Emma and Pip set off on a magical journey, meeting talking trees, singing birds, and dancing fireflies. Together, they reminded everyone that magic comes from believing, being kind, and seeing wonder in ordinary moments. The forest's sparkle returned, brighter than ever before.""",

        "ANIMALS": """Example Animal Story (excerpt):
Bunny the rabbit was the smallest animal in the meadow, but she had the biggest heart. All the other animals thought she was too small to help with important tasks, but Bunny believed she could do anything she set her mind to.

When the meadow's food supply started running low, all the animals worried. Bunny had an idea: she could reach the small spaces where berries grew that bigger animals couldn't access. She organized all the meadow animals to work together, each using their unique abilities.

Thanks to Bunny's clever thinking and teamwork, the meadow animals had plenty of food for the winter. Bunny learned that being small didn't mean being less important, and everyone learned that working together makes everyone stronger.""",

        "PROBLEM-SOLVING": """Example Problem-Solving Story (excerpt):
Jake loved building things, but his favorite toy robot had stopped working. He tried everything - new batteries, checking all the parts, even asking his parents for help. Nothing seemed to work.

Instead of giving up, Jake decided to think like a scientist. He carefully took the robot apart and examined each piece. He drew pictures of what he saw and made notes about how everything connected.

After studying the problem, Jake realized that a small wire had come loose. With patience and careful attention, he fixed the wire and put the robot back together. The robot worked perfectly! Jake learned that problems can be solved by being patient, observant, and not giving up.""",

        "EVERYDAY": """Example Everyday Story (excerpt):
Every morning, Maya helped her family by making her bed and setting the breakfast table. She loved these small routines because they made her feel capable and responsible.

One day, Maya's little brother was feeling sad because he couldn't tie his shoes. Maya remembered how patient her parents had been when teaching her, so she sat down with her brother and showed him step by step.

After practicing together every morning, Maya's brother learned to tie his shoes. He was so proud! Maya felt happy too, because she had learned that helping others and being patient feels wonderful. It became their special morning routine.""",

        "MIXED": """Example Mixed Story (excerpt):
Emma loved her everyday life, but she also dreamed of magical adventures. One ordinary Tuesday, something extraordinary happened. While playing in her backyard, Emma discovered a small door that appeared in the base of an old oak tree.

Curious, Emma opened the door and found herself in a magical forest where animals could talk and flowers glowed with soft light. A friendly rabbit named Pip asked for her help - the forest's magic was fading because children had stopped believing in wonder.

Emma used her problem-solving skills from school and her kindness to help the forest creatures. She organized a plan to show the magic to other children, proving that everyday life can be full of wonder if you look for it. The forest's magic grew stronger, and Emma learned that adventure and friendship can be found anywhere."""
    }
    
    def __init__(self, model: str = "gpt-3.5-turbo"):
        """Initialize the storyteller agent."""
        super().__init__(model)
        self.temperature = 0.8  # Higher temperature for more creative storytelling
    
    def generate_story(
        self,
        user_request: str,
        category: str = "MIXED",
        use_story_arc: bool = True,
        arc_type: str = "three_act"
    ) -> str:
        """
        Generate a bedtime story based on the user request.
        
        Args:
            user_request: The user's story request
            category: The story category (from categorizer)
            use_story_arc: Whether to use structured story arc guidance
            arc_type: Type of story arc ("three_act" or "five_part")
            
        Returns:
            The generated story text
        """
        # Build the base prompt
        base_prompt = PromptTemplate.create_story_prompt_base()
        
        # Get age guidelines
        guidelines = get_age_guidelines()
        
        # Get story arc guidance if requested
        arc_guidance = ""
        if use_story_arc:
            arc_guidance = StoryArc.format_arc_guidance(arc_type)
        
        # Get category-specific example
        example = self.CATEGORY_EXAMPLES.get(category, self.CATEGORY_EXAMPLES["MIXED"])
        
        # Format the prompt with all components
        prompt = PromptTemplate.format_prompt(
            base_prompt,
            variables={
                "guidelines": guidelines,
                "user_request": user_request
            },
            examples=[example],
            additional_guidelines=arc_guidance
        )
        
        # Add category-specific instruction
        category_instruction = f"\n\nSTORY CATEGORY: {category}\n"
        category_instruction += f"Please create a story that fits this category: {self._get_category_description(category)}\n"
        prompt += category_instruction
        
        # Generate the story
        story = self.call_model(
            prompt=prompt,
            max_tokens=2000,
            temperature=self.temperature
        )
        
        return story.strip()
    
    def _get_category_description(self, category: str) -> str:
        """Get a description for the category."""
        descriptions = {
            "ADVENTURE": "Focus on exploration, discovery, and exciting journeys with clear goals and obstacles.",
            "FRIENDSHIP": "Emphasize relationships, helping others, teamwork, and the value of friendship.",
            "MAGIC/FANTASY": "Include magical elements, wonder, and fantasy creatures while keeping it age-appropriate.",
            "ANIMALS": "Feature animals as main characters with human-like qualities and emotions.",
            "PROBLEM-SOLVING": "Show creative problem-solving, overcoming challenges through thinking and persistence.",
            "EVERYDAY": "Focus on relatable situations, family, school, and normal life experiences.",
            "MIXED": "Combine elements from multiple categories to create a rich, engaging story."
        }
        return descriptions.get(category, descriptions["MIXED"])

