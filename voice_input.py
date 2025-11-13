#!/usr/bin/env python3
"""
Voice input module for the AI Character Bot.
Handles speech recognition to convert user speech to text.
"""

import speech_recognition as sr
from typing import Optional


class VoiceInput:
    """Handles voice input through speech recognition."""
    
    def __init__(self):
        """Initialize the voice input system."""
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Adjust for ambient noise on initialization
        print("Calibrating microphone for ambient noise... Please wait.")
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Microphone calibrated!")
    
    def listen(self, timeout: int = 10, phrase_time_limit: int = 10) -> Optional[str]:
        """
        Listen for speech input and convert to text.
        
        Args:
            timeout: Maximum time to wait for phrase to start (seconds)
            phrase_time_limit: Maximum time for the phrase (seconds)
        
        Returns:
            Transcribed text, or None if recognition fails
        """
        try:
            with self.microphone as source:
                print("Listening...")
                audio = self.recognizer.listen(
                    source, 
                    timeout=timeout, 
                    phrase_time_limit=phrase_time_limit
                )
            
            print("Processing speech...")
            # Use Google's speech recognition
            text = self.recognizer.recognize_google(audio)
            return text
        
        except sr.WaitTimeoutError:
            print("No speech detected within timeout period.")
            return None
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from speech recognition service; {e}")
            return None
        except Exception as e:
            print(f"Error during speech recognition: {e}")
            return None
    
    def listen_continuous(self, callback, timeout: int = 10):
        """
        Listen continuously and call callback with recognized text.
        
        Args:
            callback: Function to call with recognized text
            timeout: Timeout for each listening session
        """
        while True:
            text = self.listen(timeout=timeout)
            if text:
                callback(text)
