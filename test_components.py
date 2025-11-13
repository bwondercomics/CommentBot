#!/usr/bin/env python3
"""
Simple test script to verify CommentBot components work correctly.
"""

import os
import sys
from dotenv import load_dotenv


def test_imports():
    """Test that all required modules can be imported."""
    print("Testing imports...")
    try:
        import mss
        import speech_recognition as sr
        import pyttsx3
        from PIL import Image
        import openai
        print("✓ All required packages imported successfully")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        print("Please run: pip install -r requirements.txt")
        return False


def test_env_config():
    """Test that environment configuration is set up."""
    print("\nTesting environment configuration...")
    load_dotenv()
    
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key or api_key == 'your_openai_api_key_here':
        print("✗ OpenAI API key not configured")
        print("Please copy .env.example to .env and add your API key")
        return False
    
    print("✓ Environment configuration looks good")
    return True


def test_screen_capture():
    """Test screen capture functionality."""
    print("\nTesting screen capture...")
    try:
        from screen_capture import ScreenCapture
        
        sc = ScreenCapture()
        monitor_count = sc.get_monitor_count()
        print(f"✓ Screen capture working - {monitor_count} monitor(s) detected")
        
        # Try to capture
        img = sc.capture_screen()
        if img:
            print(f"✓ Successfully captured screen ({img.size[0]}x{img.size[1]})")
        else:
            print("✗ Screen capture returned None")
            return False
        
        return True
    except Exception as e:
        print(f"✗ Screen capture error: {e}")
        return False


def test_voice_output():
    """Test voice output functionality."""
    print("\nTesting voice output...")
    try:
        from voice_output import VoiceOutput
        
        vo = VoiceOutput()
        print("✓ Voice output initialized")
        
        print("Testing speech (you should hear this)...")
        vo.speak("Testing voice output. Can you hear me?", blocking=True)
        print("✓ Voice output test completed")
        
        return True
    except Exception as e:
        print(f"✗ Voice output error: {e}")
        return False


def test_voice_input():
    """Test voice input functionality."""
    print("\nTesting voice input...")
    try:
        from voice_input import VoiceInput
        
        print("Initializing voice input (this may take a moment)...")
        vi = VoiceInput()
        print("✓ Voice input initialized")
        
        print("\nWARNING: Skipping actual microphone test")
        print("To test microphone, run the full application with: python commentbot.py")
        
        return True
    except Exception as e:
        print(f"✗ Voice input error: {e}")
        print("Make sure you have a microphone connected and permissions granted")
        return False


def main():
    """Run all tests."""
    print("=== CommentBot Component Tests ===\n")
    
    results = []
    results.append(("Imports", test_imports()))
    results.append(("Environment", test_env_config()))
    results.append(("Screen Capture", test_screen_capture()))
    results.append(("Voice Output", test_voice_output()))
    results.append(("Voice Input", test_voice_input()))
    
    print("\n=== Test Summary ===")
    all_passed = True
    for name, passed in results:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status}: {name}")
        if not passed:
            all_passed = False
    
    if all_passed:
        print("\n✓ All tests passed! You can run: python commentbot.py")
        return 0
    else:
        print("\n✗ Some tests failed. Please fix the issues above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
