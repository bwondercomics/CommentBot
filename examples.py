#!/usr/bin/env python3
"""
Example: Using CommentBot components programmatically.
This shows how to use individual components for custom applications.
"""

import os
from dotenv import load_dotenv


def example_text_only_chat():
    """Example: Simple text-based chat without voice or screen sharing."""
    print("=== Example 1: Text-Only Chat ===\n")
    
    load_dotenv()
    from ai_character import AICharacter
    
    # Create AI character
    ai = AICharacter(
        api_key=os.getenv('OPENAI_API_KEY'),
        character_name="Buddy",
        personality="enthusiastic and cheerful assistant"
    )
    
    # Have a conversation
    messages = [
        "Hello! What's your name?",
        "What can you help me with?",
        "Tell me a joke!"
    ]
    
    for msg in messages:
        print(f"You: {msg}")
        response = ai.chat(msg)
        print(f"Buddy: {response}\n")


def example_screen_vision():
    """Example: Share screen with AI for visual analysis."""
    print("=== Example 2: Screen Vision ===\n")
    
    load_dotenv()
    from ai_character import AICharacter
    from screen_capture import ScreenCapture
    
    # Create components
    ai = AICharacter(
        api_key=os.getenv('OPENAI_API_KEY'),
        character_name="Observer",
        personality="observant and detail-oriented analyst"
    )
    screen = ScreenCapture()
    
    # Capture and analyze screen
    print(f"Capturing screen (monitors available: {screen.get_monitor_count()})...")
    screen_data = screen.capture_as_base64()
    
    if screen_data:
        print("Screen captured! Asking AI to describe it...")
        response = ai.chat("What do you see on my screen? Please describe it in detail.", screen_data)
        print(f"Observer: {response}")
    else:
        print("Failed to capture screen")


def example_voice_conversation():
    """Example: Voice-only conversation without screen sharing."""
    print("=== Example 3: Voice Conversation ===\n")
    
    load_dotenv()
    from ai_character import AICharacter
    from voice_input import VoiceInput
    from voice_output import VoiceOutput
    
    # Create components
    ai = AICharacter(
        api_key=os.getenv('OPENAI_API_KEY'),
        character_name="Chatty",
        personality="talkative and friendly conversationalist"
    )
    voice_in = VoiceInput()
    voice_out = VoiceOutput()
    
    print("Speak something (you have 10 seconds)...")
    
    # Listen for input
    user_text = voice_in.listen(timeout=10)
    
    if user_text:
        print(f"You said: {user_text}")
        
        # Get AI response
        response = ai.chat(user_text)
        print(f"Chatty: {response}")
        
        # Speak response
        voice_out.speak(response, blocking=True)
    else:
        print("No speech detected")


def example_custom_workflow():
    """Example: Custom workflow combining components."""
    print("=== Example 4: Custom Workflow ===\n")
    
    load_dotenv()
    from ai_character import AICharacter
    from screen_capture import ScreenCapture
    
    # Create a coding assistant
    ai = AICharacter(
        api_key=os.getenv('OPENAI_API_KEY'),
        character_name="CodeReviewer",
        personality="experienced software engineer who gives constructive code reviews"
    )
    screen = ScreenCapture()
    
    # Simulate a code review workflow
    print("Starting automated code review...")
    
    # Capture screen
    screen_data = screen.capture_as_base64()
    
    if screen_data:
        # Ask for code review
        review_request = (
            "Please review the code visible on my screen. "
            "Look for: 1) Potential bugs, 2) Code quality issues, "
            "3) Performance concerns, and 4) Best practice violations. "
            "Provide specific, actionable feedback."
        )
        
        print("Analyzing code...")
        response = ai.chat(review_request, screen_data)
        print(f"\nCode Review from CodeReviewer:\n{response}")


def main():
    """Run examples."""
    print("CommentBot Component Examples\n")
    print("Choose an example to run:")
    print("1. Text-Only Chat")
    print("2. Screen Vision Analysis")
    print("3. Voice Conversation")
    print("4. Custom Coding Assistant Workflow")
    print("0. Exit")
    
    choice = input("\nEnter choice (0-4): ").strip()
    
    examples = {
        '1': example_text_only_chat,
        '2': example_screen_vision,
        '3': example_voice_conversation,
        '4': example_custom_workflow
    }
    
    if choice in examples:
        try:
            examples[choice]()
        except Exception as e:
            print(f"\nError running example: {e}")
            print("Make sure your .env file is configured correctly")
    elif choice == '0':
        print("Goodbye!")
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
