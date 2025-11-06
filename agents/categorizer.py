"""Story categorizer agent that classifies story requests into types."""

from typing import Dict, Tuple
from agents.base_agent import BaseAgent
from prompts.prompt_templates import PromptTemplate


class CategorizerAgent(BaseAgent):
    """Agent that categorizes story requests into specific types."""
    
    CATEGORIES = {
        "ADVENTURE": {
            "description": "Stories about journeys, quests, exploration, discovery",
            "keywords": ["journey", "quest", "explore", "adventure", "discover", "travel"]
        },
        "FRIENDSHIP": {
            "description": "Stories about relationships, helping friends, teamwork",
            "keywords": ["friend", "friendship", "team", "together", "help", "relationship"]
        },
        "MAGIC/FANTASY": {
            "description": "Stories with magical elements, fantasy creatures, wonder",
            "keywords": ["magic", "fantasy", "wizard", "dragon", "fairy", "spell", "enchanted"]
        },
        "ANIMALS": {
            "description": "Stories featuring animals as main characters",
            "keywords": ["animal", "cat", "dog", "bunny", "bird", "elephant", "tiger"]
        },
        "PROBLEM-SOLVING": {
            "description": "Stories about overcoming challenges, puzzles, creativity",
            "keywords": ["problem", "solve", "challenge", "puzzle", "creative", "fix"]
        },
        "EVERYDAY": {
            "description": "Stories about normal life situations, school, family",
            "keywords": ["school", "family", "home", "everyday", "normal", "daily"]
        },
        "MIXED": {
            "description": "Stories that combine multiple categories",
            "keywords": []
        }
    }
    
    def __init__(self, model: str = "gpt-3.5-turbo"):
        """Initialize the categorizer agent."""
        super().__init__(model)
        self.temperature = 0.3  # Lower temperature for more consistent categorization
    
    def categorize(self, user_request: str) -> Tuple[str, str]:
        """
        Categorize a story request.
        
        Args:
            user_request: The user's story request text
            
        Returns:
            Tuple of (category_name, explanation)
        """
        prompt_base = PromptTemplate.create_categorization_prompt_base()
        prompt = PromptTemplate.format_prompt(
            prompt_base,
            variables={"user_request": user_request}
        )
        
        response = self.call_model(
            prompt=prompt,
            max_tokens=200,
            temperature=self.temperature
        )
        
        # Parse the response to extract category and explanation
        category, explanation = self._parse_response(response)
        
        return category, explanation
    
    def _parse_response(self, response: str) -> Tuple[str, str]:
        """
        Parse the LLM response to extract category and explanation.
        
        Args:
            response: Raw response from the LLM
            
        Returns:
            Tuple of (category_name, explanation)
        """
        # Clean up the response
        response = response.strip()
        
        # Try to find a category name (uppercase, matches one of our categories)
        category = None
        explanation = response
        
        # Check if response starts with a category name
        for cat in self.CATEGORIES.keys():
            if response.upper().startswith(cat):
                category = cat
                # Extract explanation (everything after the category)
                explanation = response[len(cat):].strip()
                # Remove common prefixes/suffixes
                explanation = explanation.lstrip(":-").strip()
                break
        
        # If no category found, try to extract it from the response
        if not category:
            # Look for category mentioned in the response
            for cat in self.CATEGORIES.keys():
                if cat in response.upper():
                    category = cat
                    break
        
        # Default to MIXED if we can't determine
        if not category:
            category = "MIXED"
            explanation = "Could not determine specific category. Defaulting to MIXED."
        
        # If explanation is too short or empty, use a default
        if not explanation or len(explanation) < 10:
            explanation = f"This story request fits the {category} category."
        
        return category, explanation
    
    def get_category_info(self, category: str) -> Dict:
        """
        Get information about a specific category.
        
        Args:
            category: The category name
            
        Returns:
            Dictionary with category information
        """
        return self.CATEGORIES.get(category.upper(), self.CATEGORIES["MIXED"])

