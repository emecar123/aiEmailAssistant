def test_home(client):
    r = client.get("/")
    assert r.status_code == 200

def test_compose_redirects_to_result(client, monkeypatch):
    import app.routes as routes_mod

    def fake_generate(self, email_text, tone):
        return "Hello,\n\nThanks for your message. We will help you shortly.\n\nBest regards,"
    monkeypatch.setattr(routes_mod.AiService, "generate_reply", fake_generate)

    resp = client.post("/compose", data={
        "original_email": "Hi, I need help with my account.",
        "tone": "Professional",
    }, follow_redirects=False)

    assert resp.status_code == 302
    assert "/result/" in resp.headers["Location"]
