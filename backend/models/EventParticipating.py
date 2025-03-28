from . import db
from sqlalchemy.dialects.postgresql import UUID
import uuid


class EventParticipating(db.Model):
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    user_id = db.Column(UUID, db.ForeignKey('users.user_id'), nullable=False)
    event_id = db.Column(UUID, db.ForeignKey('events.event_id'), nullable=False)
