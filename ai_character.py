#!/usr/bin/env python3
"""
AI Character module for the CommentBot.
Handles interaction with OpenAI's API including vision capabilities.
"""

import os
from typing import List, Dict, Optional
from openai import OpenAI


class AICharacter:
    """Manages AI character personality and interactions."""
    
    def __init__(
        self, 
        api_key: str,
        character_name: str = "Assistant",
        personality: str = "friendly and helpful AI companion"
    ):
        """
        Initialize the AI character.
        
        Args:
            api_key: OpenAI API key
            character_name: Name of the character
            personality: Personality description for the system prompt
        """
        self.client = OpenAI(api_key=api_key)
        self.character_name = character_name
        self.personality = personality
        self.conversation_history: List[Dict] = []
        
        # Initialize with system prompt
        self.system_prompt = (
            f"You are {character_name}, a {personality}. "
            f"You can see the user's screen when they share it with you. "
            f"Respond naturally and conversationally. Keep responses concise but engaging. "
            f"When you see something on the screen, comment on it naturally as part of the conversation."
        )
        
        self.conversation_history.append({
            "role": "system",
            "content": self.system_prompt
        })
    
    def chat(self, user_message: str, screen_image_base64: Optional[str] = None) -> str:
        """
        Send a message to the AI character and get a response.
        
        Args:
            user_message: The user's text input
            screen_image_base64: Optional base64-encoded screenshot
        
        Returns:
            AI character's response
        """
        # Build the message
        if screen_image_base64:
            # Use vision API when screen is shared
            message_content = [
                {"type": "text", "text": user_message},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{screen_image_base64}"
                    }
                }
            ]
        else:
            message_content = user_message
        
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": message_content
        })
        
        try:
            # Get response from OpenAI
            response = self.client.chat.completions.create(
                model="gpt-4o" if screen_image_base64 else "gpt-4o-mini",
                messages=self.conversation_history,
                max_tokens=500,
                temperature=0.7
            )
            
            # Extract the assistant's response
            assistant_message = response.choices[0].message.content
            
            # Add assistant response to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            # Keep conversation history manageable (keep last 20 messages + system)
            if len(self.conversation_history) > 21:
                self.conversation_history = [self.conversation_history[0]] + self.conversation_history[-20:]
            
            return assistant_message
        
        except Exception as e:
            error_msg = f"Error communicating with AI: {e}"
            print(error_msg)
            return f"Sorry, I'm having trouble responding right now. Error: {str(e)}"
    
    def reset_conversation(self):
        """Reset the conversation history."""
        self.conversation_history = [{
            "role": "system",
            "content": self.system_prompt
        }]
    
    def get_conversation_length(self) -> int:
        """Get the number of messages in the conversation."""
        return len(self.conversation_history) - 1  # Exclude system message
