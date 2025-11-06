"""Base agent class for LLM interactions."""

import os
from typing import Optional
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class BaseAgent:
    """Base class for all agents that interact with the LLM."""
    
    def __init__(self, model: str = "gpt-3.5-turbo"):
        """
        Initialize the base agent.
        
        Args:
            model: The OpenAI model to use (default: gpt-3.5-turbo)
        """
        self.model = model
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "OPENAI_API_KEY not found in environment variables. "
                "Please set it in your .env file."
            )
        openai.api_key = self.api_key
    
    def call_model(
        self,
        prompt: str,
        max_tokens: int = 3000,
        temperature: float = 0.1,
        system_message: Optional[str] = None
    ) -> str:
        """
        Call the OpenAI model with a prompt.
        
        Args:
            prompt: The user prompt/message
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature (0.0-2.0)
            system_message: Optional system message for context
            
        Returns:
            The model's response text
        """
        messages = []
        
        if system_message:
            messages.append({"role": "system", "content": system_message})
        
        messages.append({"role": "user", "content": prompt})
        
        resp = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            stream=False,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        
        return resp.choices[0].message["content"]  # type: ignore

