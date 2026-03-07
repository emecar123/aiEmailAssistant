from app.services.email_service import EmailService
from app import db

def test_create_and_save_final_reply(app_instance):
    with app_instance.app_context():
        entry = EmailService.create_email_entry("Hello, can we reschedule?", "Professional")
        assert entry.id is not None
        assert entry.generated_reply is None

        EmailService.update_generated_reply(entry, "Certainly, we can reschedule.")
        EmailService.save_final_reply(entry, "Certainly, we can reschedule to next week.")
        db.session.refresh(entry)
        assert "next week" in entry.final_reply
