# CommentBot

An AI-driven character with voice interaction that you can talk to while on your PC, with the ability to share your screen - similar to what DougDoug does on his streams!

## Features

- 🎤 **Voice Input**: Speak naturally to the AI character using your microphone
- 🔊 **Voice Output**: The AI responds with a natural voice using text-to-speech
- 👁️ **Screen Sharing**: Share your screen with the AI so it can see what you're doing
- 🤖 **AI Vision**: Uses OpenAI's GPT-4 with vision to understand and comment on your screen
- 💬 **Natural Conversation**: Maintains conversation context for coherent interactions
- ⚙️ **Customizable**: Configure character name, personality, and voice settings

## Prerequisites

- Python 3.8 or higher
- OpenAI API key (get one from [OpenAI](https://platform.openai.com/api-keys))
- Microphone for voice input
- Speakers/headphones for voice output

## Installation

1. Clone this repository:
```bash
git clone https://github.com/bwondercomics/CommentBot.git
cd CommentBot
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your configuration:
```bash
cp .env.example .env
```

4. Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=your_actual_api_key_here
```

## Configuration

Edit the `.env` file to customize your AI character:

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `CHARACTER_NAME`: Name of your AI character (default: "Assistant")
- `CHARACTER_PERSONALITY`: Personality description (default: "friendly and helpful AI companion")
- `VOICE_RATE`: Speech speed in words per minute (default: 150)
- `VOICE_VOLUME`: Volume level from 0.0 to 1.0 (default: 0.9)

## Usage

Run the application:
```bash
python commentbot.py
```

### Voice Commands

Once running, you can:
- **Chat naturally**: Just speak to have a conversation
- **Share your screen**: Say "show screen" or "look at my screen"
- **Reset conversation**: Say "reset" to start fresh
- **Exit**: Say "exit" or "quit" to close the application

### Example Interactions

```
You: Hello! How are you today?
Assistant: I'm doing great! How can I help you today?

You: Look at my screen, what do you see?
Assistant: I can see you have a code editor open with Python code...

You: What do you think of this code?
Assistant: The code looks well-structured! I notice you're using...
```

## How It Works

CommentBot integrates several components:

1. **Screen Capture** (`screen_capture.py`): Captures screenshots using MSS
2. **Voice Input** (`voice_input.py`): Converts speech to text using Google Speech Recognition
3. **Voice Output** (`voice_output.py`): Converts AI responses to speech using pyttsx3
4. **AI Character** (`ai_character.py`): Manages personality and OpenAI API interactions
5. **Main Application** (`commentbot.py`): Orchestrates all components

## Troubleshooting

### Audio Issues
- **Microphone not working**: Check system audio permissions and microphone settings
- **No voice output**: Ensure speakers are connected and volume is up
- **"Could not understand audio"**: Speak more clearly or check microphone quality

### API Issues
- **API key errors**: Verify your OpenAI API key is correct in `.env`
- **Rate limiting**: OpenAI has rate limits; wait a moment and try again
- **Vision not working**: Ensure you're using a plan that supports GPT-4 with vision

### Screen Capture Issues
- **Black screen**: Some applications block screen capture for DRM
- **Multiple monitors**: The app captures the primary monitor by default

## Cost Considerations

Using this application incurs OpenAI API costs:
- Text-only chat: Uses GPT-4o-mini (lower cost)
- Chat with screen sharing: Uses GPT-4o (higher cost due to vision)

Monitor your API usage on the [OpenAI dashboard](https://platform.openai.com/usage).

## Privacy & Security

- Your API key is stored locally in `.env` (never commit this file!)
- Conversations are sent to OpenAI's API
- Screenshots are only sent when you request screen sharing
- No data is stored permanently by this application

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## License

This project is open source and available under the MIT License.

## Credits

Inspired by DougDoug's AI stream interactions.

Built with:
- [OpenAI API](https://openai.com/) for AI capabilities
- [SpeechRecognition](https://github.com/Uberi/speech_recognition) for voice input
- [pyttsx3](https://github.com/nateshmbhat/pyttsx3) for voice output
- [MSS](https://github.com/BoboTiG/python-mss) for screen capture
