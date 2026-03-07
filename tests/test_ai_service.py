class DummyResp:
    def __init__(self, output_text):
        self.output_text = output_text

class DummyResponses:
    def create(self, **kwargs):
        return DummyResp("Hello John,\n\nThank you for your message. We will assist shortly.\n\nBest regards,")

class DummyClient:
    def __init__(self):
        self.responses = DummyResponses()

def test_generate_reply(monkeypatch):
    import app.services.ai_service as mod
    monkeypatch.setattr(mod, "OpenAI", lambda api_key: DummyClient())

    ai = mod.AiService(api_key="test", model="gpt-4o-mini")
    reply = ai.generate_reply("Need help", "Professional")
    assert "Thank you" in reply
