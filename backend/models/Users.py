from . import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Users(db.Model):
    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    username = db.Column(db.String(300), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(300), nullable=False)
    is_organizer = db.Column(db.Boolean, nullable=False)

    def as_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "is_organizer": self.is_organizer
        }
