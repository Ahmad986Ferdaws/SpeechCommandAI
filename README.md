# SpeechCommandAI

A real-time voice command detector and explainer using torchaudio and GPT-4.

## Features
- Upload `.wav` voice samples
- Classify commands like “stop”, “go”, “yes”
- GPT explains the command use case
- Logs stored in SQLite

## Setup
1. Add `.env` with your OpenAI API key
2. Install dependencies
3. Run: `uvicorn app.main:app --reload`
