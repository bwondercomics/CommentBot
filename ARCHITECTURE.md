# CommentBot Architecture

## Overview

CommentBot is a modular AI-driven voice assistant with screen-sharing capabilities. The architecture follows a component-based design where each module handles a specific responsibility.

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      CommentBot Main                         │
│                    (commentbot.py)                           │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                      │
        ▼                     ▼                      ▼
┌──────────────┐    ┌──────────────────┐    ┌──────────────┐
│ Voice Input  │    │   AI Character   │    │ Voice Output │
│ (voice_input)│    │ (ai_character)   │    │(voice_output)│
└──────────────┘    └──────────────────┘    └──────────────┘
                            │
                            ▼
                    ┌──────────────┐
                    │Screen Capture│
                    │(screen_cap)  │
                    └──────────────┘
```

## Components

### 1. Voice Input (voice_input.py)
**Purpose**: Convert user speech to text

**Dependencies**:
- `speech_recognition` - Core speech recognition
- `pyaudio` - Audio input handling

**Key Features**:
- Ambient noise calibration
- Configurable timeout and phrase limits
- Google Speech Recognition backend

**API**:
```python
voice_input = VoiceInput()
text = voice_input.listen(timeout=10)
```

### 2. Voice Output (voice_output.py)
**Purpose**: Convert AI responses to speech

**Dependencies**:
- `pyttsx3` - Text-to-speech engine

**Key Features**:
- Customizable speech rate and volume
- Voice selection (male/female)
- Non-blocking speech (threaded)

**API**:
```python
voice_output = VoiceOutput(rate=150, volume=0.9)
voice_output.speak("Hello world", blocking=False)
```

### 3. Screen Capture (screen_capture.py)
**Purpose**: Capture and encode screenshots

**Dependencies**:
- `mss` - Cross-platform screen capture
- `PIL/Pillow` - Image processing

**Key Features**:
- Multi-monitor support
- Image resizing for API efficiency
- Base64 encoding for API transmission

**API**:
```python
screen = ScreenCapture()
image_base64 = screen.capture_as_base64(monitor_number=1, max_size=(1024, 768))
```

### 4. AI Character (ai_character.py)
**Purpose**: Manage AI personality and interactions

**Dependencies**:
- `openai` - OpenAI API client

**Key Features**:
- GPT-4 with vision support
- Conversation history management
- Automatic model selection (GPT-4o-mini for text, GPT-4o for vision)
- Customizable personality

**API**:
```python
ai = AICharacter(api_key="...", character_name="Buddy", personality="helpful")
response = ai.chat("Hello!", screen_image_base64=None)
```

### 5. Main Application (commentbot.py)
**Purpose**: Orchestrate all components

**Key Features**:
- Environment configuration loading
- Command recognition (exit, reset, show screen)
- Main conversation loop
- Error handling

## Data Flow

### Text-Only Conversation
1. User speaks → Voice Input captures audio
2. Voice Input converts to text via Google API
3. Text sent to AI Character
4. AI Character queries OpenAI (GPT-4o-mini)
5. Response converted to speech via Voice Output
6. User hears response

### Conversation with Screen Sharing
1. User says "show screen" or similar
2. Screen Capture takes screenshot
3. Screenshot resized and encoded to base64
4. Text + Image sent to AI Character
5. AI Character queries OpenAI with vision (GPT-4o)
6. Response describes screen content
7. Response spoken via Voice Output

## Configuration Management

### Environment Variables (.env)
- `OPENAI_API_KEY` - Required for AI functionality
- `CHARACTER_NAME` - AI character name
- `CHARACTER_PERSONALITY` - System prompt personality
- `VOICE_RATE` - Speech speed (words/minute)
- `VOICE_VOLUME` - Output volume (0.0-1.0)

### Security
- API keys stored in `.env` (git-ignored)
- No credentials in source code
- Local processing only (except OpenAI API calls)

## Error Handling

Each component implements defensive error handling:
- Voice Input: Timeout and recognition errors
- Voice Output: Thread safety for concurrent speech
- Screen Capture: Monitor availability checks
- AI Character: API error handling and retry logic
- Main App: Graceful degradation

## Performance Considerations

### Optimization Strategies
1. **Screen capture** resized to 1024x768 max (reduces API costs)
2. **Model selection** - GPT-4o-mini for text (cheaper), GPT-4o only for vision
3. **Conversation history** limited to 20 messages (prevents token overflow)
4. **Non-blocking speech** prevents UI freezing

### Resource Usage
- Memory: ~100MB base + conversation history
- CPU: Minimal except during speech recognition
- Network: API calls only (no local AI model)

## Extensibility

The modular design allows easy extension:

### Adding New Features
- **Custom commands**: Extend command recognition in `commentbot.py`
- **New AI models**: Swap OpenAI client in `ai_character.py`
- **Alternative TTS**: Replace pyttsx3 in `voice_output.py`
- **Recording**: Add audio recording to `voice_input.py`

### Integration
All components can be used independently (see `examples.py`):
```python
from screen_capture import ScreenCapture
from ai_character import AICharacter

# Use components in custom application
screen = ScreenCapture()
ai = AICharacter(api_key="...")
```

## Testing Strategy

### Unit Testing
- `test_components.py` validates each module independently
- Import verification
- Configuration checking
- Functional testing (where applicable)

### Integration Testing
- Manual testing via main application
- Voice loop testing
- Screen sharing validation

## Future Enhancements

Potential improvements:
1. **Multiple AI models** - Support for Claude, Gemini, etc.
2. **Wake word detection** - "Hey Assistant" activation
3. **Conversation persistence** - Save/load chat history
4. **GUI interface** - Visual controls and settings
5. **Streaming responses** - Real-time TTS for long responses
6. **Local models** - Privacy-focused local AI option
7. **Multi-language** - Support for non-English conversations

## Dependencies Graph

```
commentbot.py
├── voice_input.py
│   ├── speech_recognition
│   └── pyaudio
├── voice_output.py
│   └── pyttsx3
├── screen_capture.py
│   ├── mss
│   └── pillow
├── ai_character.py
│   └── openai
└── python-dotenv
```

## Platform Support

- **Windows**: Full support
- **macOS**: Full support (requires microphone permissions)
- **Linux**: Full support (may need additional audio setup)

## License

MIT License - See LICENSE file
