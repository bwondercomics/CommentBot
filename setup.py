#!/usr/bin/env python3
"""
Quick setup script for CommentBot.
Helps users get started quickly.
"""

import os
import sys
import shutil


def setup():
    """Run the setup process."""
    print("=== CommentBot Setup ===\n")
    
    # Check if .env exists
    if not os.path.exists('.env'):
        if os.path.exists('.env.example'):
            print("Creating .env file from .env.example...")
            shutil.copy('.env.example', '.env')
            print("✓ Created .env file")
            print("\n⚠️  IMPORTANT: You need to edit .env and add your OpenAI API key!")
            print("   Open .env in a text editor and replace 'your_openai_api_key_here'")
            print("   with your actual API key from https://platform.openai.com/api-keys")
        else:
            print("✗ .env.example not found!")
            return False
    else:
        print("✓ .env file already exists")
    
    # Check if dependencies are installed
    print("\nChecking dependencies...")
    try:
        import openai
        import mss
        import speech_recognition
        import pyttsx3
        from PIL import Image
        print("✓ All dependencies are installed")
    except ImportError as e:
        print(f"✗ Missing dependency: {e}")
        print("\nPlease install dependencies with:")
        print("  pip install -r requirements.txt")
        return False
    
    # Quick test
    print("\nRunning quick component test...")
    os.system(f"{sys.executable} test_components.py")
    
    print("\n=== Setup Complete ===")
    print("\nNext steps:")
    print("1. Edit .env and add your OpenAI API key")
    print("2. Run the application: python commentbot.py")
    print("\nEnjoy chatting with your AI character!")
    
    return True


if __name__ == "__main__":
    setup()
