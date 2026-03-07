# Step-by-Step Student Guide — AI Email Reply Assistant

## Goal
Build a Flask web app that accepts an incoming email, uses the OpenAI API to draft a reply, and stores both the original email and reply in a SQLite database.

---

## Milestone 1 — Setup
1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env`
4. Add your OpenAI API key:
   ```text
   OPENAI_API_KEY=your_key_here
   ```

✅ Checkpoint: `python run.py` starts the app.

---

## Milestone 2 — Understand the Folder Structure
Review:
- `app/routes.py` -> HTTP request handling
- `app/models.py` -> database schema
- `app/services/email_service.py` -> database logic
- `app/services/ai_service.py` -> OpenAI integration
- `app/templates/` -> frontend pages

✅ Checkpoint: Explain in one sentence what each layer does.

---

## Milestone 3 — Database Layer
The database table is `EmailReply`.

Fields:
- `original_email`
- `tone`
- `generated_reply`
- `final_reply`
- `created_at`

✅ Checkpoint: Submit one email and confirm data is saved.

---

## Milestone 4 — Business Logic Layer
Review `email_service.py`.

It handles:
- creating a new email entry
- updating the AI-generated draft
- saving the final edited reply
- listing history

✅ Checkpoint: Confirm routes call the service instead of DB code directly.

---

## Milestone 5 — AI Integration
Review `ai_service.py`.

The AI service:
1. Accepts the original email and tone
2. Sends them to OpenAI
3. Returns a drafted reply

✅ Checkpoint: Paste a short email and generate a reply successfully.

---

## Milestone 6 — Frontend Pages
Pages included:
- `/` -> home
- `/compose` -> form to submit email
- `/result/<id>` -> generated reply
- `/history` -> past entries

✅ Checkpoint: Navigate all pages successfully.

---

## Milestone 7 — Save Final Reply
On the result page, edit the draft and save it.

✅ Checkpoint: Refresh the page and confirm the edited reply is stored.

---

## Milestone 8 — Testing
Run:
```bash
pytest -q
```

Tests cover:
- business logic
- AI service with a mocked client
- route behavior

✅ Checkpoint: All tests pass.

---

## Milestone 9 — Docker (Optional)
Build:
```bash
docker build -t ai-email-assistant .
```

Run:
```bash
docker run --env-file .env -p 5000:5000 ai-email-assistant
```

✅ Checkpoint: App runs in a container.

---

## Reflection Questions
1. What part of this app is the business logic?
2. Why is AI logic in a service file instead of routes?
3. What could go wrong if the API key is hardcoded?
4. What would you test before deploying this app?

---

## Extension Ideas
- Add authentication for the history page
- Add tone options like “empathetic” or “direct”
- Add email summarization
- Add export to PDF
- Add usage analytics dashboard
