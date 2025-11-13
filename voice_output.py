#!/usr/bin/env python3
"""
Voice output module for the AI Character Bot.
Handles text-to-speech to give the AI character a voice.
"""

import pyttsx3
import threading
from queue import Queue


class VoiceOutput:
    """Handles text-to-speech output."""
    
    def __init__(self, rate: int = 150, volume: float = 0.9):
        """
        Initialize the voice output system.
        
        Args:
            rate: Speech rate in words per minute
            volume: Volume level (0.0 to 1.0)
        """
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
        
        # Use a queue for thread-safe speaking
        self.speech_queue = Queue()
        self.is_speaking = False
        
        # Get available voices
        voices = self.engine.getProperty('voices')
        if voices:
            # Try to set a pleasant voice (prefer female voices for variety)
            for voice in voices:
                if 'female' in voice.name.lower() or 'zira' in voice.name.lower():
                    self.engine.setProperty('voice', voice.id)
                    break
    
    def speak(self, text: str, blocking: bool = False):
        """
        Speak the given text.
        
        Args:
            text: Text to speak
            blocking: If True, wait for speech to complete before returning
        """
        if blocking:
            self.engine.say(text)
            self.engine.runAndWait()
        else:
            # Speak in a separate thread to avoid blocking
            thread = threading.Thread(target=self._speak_thread, args=(text,))
            thread.daemon = True
            thread.start()
    
    def _speak_thread(self, text: str):
        """Internal method to speak in a separate thread."""
        self.is_speaking = True
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        finally:
            self.is_speaking = False
    
    def stop(self):
        """Stop current speech."""
        if self.is_speaking:
            self.engine.stop()
    
    def set_rate(self, rate: int):
        """Set speech rate in words per minute."""
        self.engine.setProperty('rate', rate)
    
    def set_volume(self, volume: float):
        """Set volume (0.0 to 1.0)."""
        self.engine.setProperty('volume', volume)
    
    def list_voices(self):
        """Print available voices."""
        voices = self.engine.getProperty('voices')
        print("Available voices:")
        for idx, voice in enumerate(voices):
            print(f"{idx}: {voice.name} ({voice.id})")
    
    def set_voice(self, voice_id: str):
        """Set voice by ID."""
        self.engine.setProperty('voice', voice_id)
