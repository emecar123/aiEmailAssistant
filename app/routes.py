from flask import Blueprint, render_template, request, redirect, url_for, current_app, flash
from app.services.email_service import EmailService
from app.services.ai_service import AiService

bp = Blueprint("main", __name__)

VALID_TONES = ["Professional", "Friendly", "Formal"]

@bp.get("/")
def index():
    return render_template("index.html")

@bp.route("/compose", methods=["GET", "POST"])
def compose():
    if request.method == "GET":
        return render_template("compose.html", tones=VALID_TONES)

    original_email = (request.form.get("original_email") or "").strip()
    tone = (request.form.get("tone") or "Professional").strip()

    if not original_email:
        flash("Please paste the incoming email.", "error")
        return render_template("compose.html", tones=VALID_TONES), 400

    if tone not in VALID_TONES:
        flash("Invalid tone selected.", "error")
        return render_template("compose.html", tones=VALID_TONES), 400

    max_len = current_app.config.get("MAX_EMAIL_LENGTH", 4000)
    if len(original_email) > max_len:
        flash(f"Email is too long. Max length is {max_len} characters.", "error")
        return render_template("compose.html", tones=VALID_TONES), 400

    entry = EmailService.create_email_entry(original_email, tone)

    ai = AiService(
        api_key=current_app.config["OPENAI_API_KEY"],
        model=current_app.config["OPENAI_MODEL"],
    )
    generated = ai.generate_reply(original_email, tone)
    EmailService.update_generated_reply(entry, generated)

    return redirect(url_for("main.result", entry_id=entry.id))

@bp.get("/result/<int:entry_id>")
def result(entry_id: int):
    entry = EmailService.get_entry(entry_id)
    if not entry:
        return "Not found", 404
    return render_template("result.html", entry=entry)

@bp.post("/result/<int:entry_id>/save")
def save(entry_id: int):
    entry = EmailService.get_entry(entry_id)
    if not entry:
        return "Not found", 404

    final_reply = (request.form.get("final_reply") or "").strip()
    if not final_reply:
        flash("Final reply cannot be empty.", "error")
        return redirect(url_for("main.result", entry_id=entry.id))

    EmailService.save_final_reply(entry, final_reply)
    flash("Final reply saved.", "success")
    return redirect(url_for("main.result", entry_id=entry.id))

@bp.get("/history")
def history():
    entries = EmailService.list_entries()
    return render_template("history.html", entries=entries)
