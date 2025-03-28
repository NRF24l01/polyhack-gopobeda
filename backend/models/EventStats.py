from . import db
from sqlalchemy.dialects.postgresql import UUID
import uuid


class EventStats(db.Model):
    stats_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    user_id = db.Column(UUID, db.ForeignKey('users.user_id'), nullable=False)
    event_id = db.Column(UUID, db.ForeignKey('events.event_id'), nullable=False)

    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    participants = db.Column(db.Integer, nullable=False)
    conversion = db.Column(db.Float, nullable=False)

    def as_dict(self):
        return {
            'stats_id': self.stats_id,
            'views': self.views,
            'likes': self.likes,
            'participants': self.participants,
            'conversion': self.conversion
        }
