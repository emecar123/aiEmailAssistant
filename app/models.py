from datetime import datetime
from app import db

class EmailReply(db.Model):
    __tablename__ = "email_replies"

    id = db.Column(db.Integer, primary_key=True)
    original_email = db.Column(db.Text, nullable=False)
    tone = db.Column(db.String(30), nullable=False, default="Professional")
    generated_reply = db.Column(db.Text, nullable=True)
    final_reply = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
