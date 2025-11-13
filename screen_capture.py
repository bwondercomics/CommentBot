#!/usr/bin/env python3
"""
Screen capture module for the AI Character Bot.
Captures screenshots that can be shared with the AI for visual context.
"""

import io
import base64
from typing import Optional
from PIL import Image
import mss


class ScreenCapture:
    """Handles screen capturing functionality."""
    
    def __init__(self):
        """Initialize the screen capture system."""
        self.sct = mss.mss()
    
    def capture_screen(self, monitor_number: int = 1) -> Optional[Image.Image]:
        """
        Capture a screenshot of the specified monitor.
        
        Args:
            monitor_number: Monitor index (1 for primary, 2+ for additional monitors)
        
        Returns:
            PIL Image object of the screenshot, or None if capture fails
        """
        try:
            # Get the monitor
            monitor = self.sct.monitors[monitor_number]
            
            # Capture the screen
            screenshot = self.sct.grab(monitor)
            
            # Convert to PIL Image
            img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
            return img
        except Exception as e:
            print(f"Error capturing screen: {e}")
            return None
    
    def capture_as_base64(self, monitor_number: int = 1, max_size: tuple = (1024, 768)) -> Optional[str]:
        """
        Capture screen and convert to base64 string for API transmission.
        
        Args:
            monitor_number: Monitor index
            max_size: Maximum dimensions to resize to (width, height)
        
        Returns:
            Base64 encoded string of the image, or None if capture fails
        """
        img = self.capture_screen(monitor_number)
        if img is None:
            return None
        
        # Resize if needed to reduce API costs
        img.thumbnail(max_size, Image.Resampling.LANCZOS)
        
        # Convert to base64
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        img_bytes = buffer.getvalue()
        img_base64 = base64.b64encode(img_bytes).decode('utf-8')
        
        return img_base64
    
    def get_monitor_count(self) -> int:
        """Get the number of available monitors."""
        return len(self.sct.monitors) - 1  # -1 because index 0 is all monitors combined
    
    def __del__(self):
        """Clean up resources."""
        if hasattr(self, 'sct'):
            self.sct.close()
