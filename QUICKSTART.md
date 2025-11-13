# Quick Start Guide

Get CommentBot up and running in 5 minutes!

## Step 1: Install Python Dependencies

```bash
pip install -r requirements.txt
```

## Step 2: Get Your OpenAI API Key

1. Go to [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Sign in or create an account
3. Click "Create new secret key"
4. Copy the key (you won't see it again!)

## Step 3: Configure CommentBot

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your favorite text editor
# Replace 'your_openai_api_key_here' with your actual API key
```

## Step 4: Run the Setup Script

```bash
python setup.py
```

This will verify all dependencies are installed correctly.

## Step 5: Start ChatBot

```bash
python commentbot.py
```

## First Conversation

Once running, try these commands:

1. **Say "Hello"** - Start a conversation
2. **Say "Show screen"** - Share your screen with the AI
3. **Say "What do you see?"** - Ask about what's on your screen
4. **Say "Exit"** - End the conversation

## Troubleshooting Quick Tips

### "No module named..." errors
```bash
pip install -r requirements.txt
```

### "Please set your OPENAI_API_KEY" error
- Check that `.env` file exists
- Verify your API key is correct (no extra spaces or quotes)

### Microphone not working
- Check system permissions for microphone access
- On macOS/Linux: Grant terminal microphone permission
- On Windows: Check Privacy settings

### No voice output
- Check that your speakers/headphones are connected
- Verify system volume is not muted
- Try adjusting `VOICE_VOLUME` in `.env`

## What's Next?

Check out the full [README.md](README.md) for:
- Advanced configuration options
- Cost optimization tips
- Privacy and security information
- Contributing guidelines

## Example Interaction

```
Listening...

You: Hello! Can you see my screen?
Assistant: Hello! I can't see your screen right now. Say "show screen" if you'd like me to look at it!

You: Show screen
Capturing screen...
Screen shared with AI
Assistant: I can see you have a terminal window open with some Python code. It looks like you're working on the CommentBot project! How can I help you with it?

You: Exit
Assistant: Goodbye! It was nice talking to you!
```

Enjoy your AI companion! 🎉
