# AI Email Reply Assistant

A beginner-friendly Flask web app that helps users draft professional email replies using the OpenAI API.

## Features
- Paste an incoming email
- AI generates a professional reply
- Store original email, AI draft, tone, and final edited reply in SQLite
- Simple history page
- Modular architecture: routes -> services -> models
- Basic tests with pytest
- Docker-ready

## Quick Start
1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and set `OPENAI_API_KEY`
4. Run the app:
   ```bash
   python run.py
   ```
5. Open http://localhost:5000

## Tests
```bash
pytest -q
```

## Docker
```bash
docker build -t ai-email-assistant .
docker run --env-file .env -p 5000:5000 ai-email-assistant
```
