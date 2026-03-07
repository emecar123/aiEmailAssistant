from app import db
from app.models import EmailReply

class EmailService:
    @staticmethod
    def create_email_entry(original_email: str, tone: str) -> EmailReply:
        entry = EmailReply(original_email=original_email, tone=tone)
        db.session.add(entry)
        db.session.commit()
        return entry

    @staticmethod
    def update_generated_reply(entry: EmailReply, generated_reply: str) -> EmailReply:
        entry.generated_reply = generated_reply
        db.session.commit()
        return entry

    @staticmethod
    def save_final_reply(entry: EmailReply, final_reply: str) -> EmailReply:
        entry.final_reply = final_reply
        db.session.commit()
        return entry

    @staticmethod
    def get_entry(entry_id: int) -> EmailReply | None:
        return EmailReply.query.get(entry_id)

    @staticmethod
    def list_entries() -> list[EmailReply]:
        return EmailReply.query.order_by(EmailReply.created_at.desc()).all()
