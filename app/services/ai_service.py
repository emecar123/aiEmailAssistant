from openai import OpenAI

class AiService:
    def __init__(self, api_key: str, model: str):
        if not api_key:
            raise ValueError("OPENAI_API_KEY is missing. Set it in your environment or .env file.")
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def generate_reply(self, email_text: str, tone: str) -> str:
        system_instructions = (
            "You are an email assistant. Draft a clear, polite, concise reply. "
            "Do not invent facts. If the incoming email asks for something specific, "
            "respond professionally and suggest reasonable next steps. "
            f"Use a {tone.lower()} tone."
        )

        response = self.client.responses.create(
            model=self.model,
            input=[
                {"role": "system", "content": system_instructions},
                {"role": "user", "content": f"Incoming email:\n{email_text}\n\nDraft a reply only."}
            ],
        )
        return response.output_text.strip()
