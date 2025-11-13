#!/usr/bin/env python3
"""
CommentBot - AI-driven character with voice and screen sharing.
Main application that integrates all components.
"""

import os
import sys
from dotenv import load_dotenv

from screen_capture import ScreenCapture
from voice_input import VoiceInput
from voice_output import VoiceOutput
from ai_character import AICharacter


class CommentBot:
    """Main application class for the AI character bot."""
    
    def __init__(self):
        """Initialize the CommentBot application."""
        # Load environment variables
        load_dotenv()
        
        # Get configuration
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key or self.api_key == 'your_openai_api_key_here':
            print("ERROR: Please set your OPENAI_API_KEY in the .env file")
            print("Copy .env.example to .env and add your API key")
            sys.exit(1)
        
        self.character_name = os.getenv('CHARACTER_NAME', 'Assistant')
        self.personality = os.getenv('CHARACTER_PERSONALITY', 'friendly and helpful AI companion')
        
        # Voice settings
        voice_rate = int(os.getenv('VOICE_RATE', '150'))
        voice_volume = float(os.getenv('VOICE_VOLUME', '0.9'))
        
        # Initialize components
        print("Initializing CommentBot...")
        self.screen_capture = ScreenCapture()
        self.voice_input = VoiceInput()
        self.voice_output = VoiceOutput(rate=voice_rate, volume=voice_volume)
        self.ai_character = AICharacter(
            api_key=self.api_key,
            character_name=self.character_name,
            personality=self.personality
        )
        
        print(f"\n{self.character_name} is ready!")
        print(f"Detected {self.screen_capture.get_monitor_count()} monitor(s)")
        print("\nCommands:")
        print("  - Just speak naturally to chat")
        print("  - Say 'show screen' or 'look at screen' to share your screen")
        print("  - Say 'exit' or 'quit' to end the conversation")
        print("  - Say 'reset' to start a new conversation")
        print("\nListening...\n")
    
    def process_user_input(self, user_text: str):
        """
        Process user input and generate AI response.
        
        Args:
            user_text: Transcribed user speech
        """
        print(f"\nYou: {user_text}")
        
        # Check for commands
        user_text_lower = user_text.lower()
        
        if user_text_lower in ['exit', 'quit', 'goodbye', 'bye']:
            response = "Goodbye! It was nice talking to you!"
            print(f"{self.character_name}: {response}")
            self.voice_output.speak(response, blocking=True)
            return False  # Signal to exit
        
        if user_text_lower in ['reset', 'new conversation', 'start over']:
            self.ai_character.reset_conversation()
            response = "Okay, let's start a fresh conversation!"
            print(f"{self.character_name}: {response}")
            self.voice_output.speak(response, blocking=True)
            return True
        
        # Check if user wants to share screen
        share_screen = any(phrase in user_text_lower for phrase in [
            'show screen', 'look at screen', 'see my screen', 
            'what do you see', 'look at this', 'check my screen'
        ])
        
        # Get AI response
        screen_data = None
        if share_screen:
            print("Capturing screen...")
            screen_data = self.screen_capture.capture_as_base64()
            if screen_data:
                print("Screen shared with AI")
        
        response = self.ai_character.chat(user_text, screen_data)
        
        print(f"{self.character_name}: {response}")
        self.voice_output.speak(response)
        
        return True  # Continue conversation
    
    def run(self):
        """Run the main application loop."""
        try:
            while True:
                # Listen for user input
                user_text = self.voice_input.listen(timeout=30)
                
                if user_text:
                    should_continue = self.process_user_input(user_text)
                    if not should_continue:
                        break
                else:
                    # No input detected, keep listening
                    continue
        
        except KeyboardInterrupt:
            print("\n\nStopping CommentBot...")
            self.voice_output.speak("Goodbye!", blocking=True)
        except Exception as e:
            print(f"\nError: {e}")
            self.voice_output.speak("Sorry, I encountered an error.", blocking=True)


def main():
    """Main entry point."""
    bot = CommentBot()
    bot.run()


if __name__ == "__main__":
    main()
