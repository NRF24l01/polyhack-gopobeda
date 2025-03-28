from . import db
from sqlalchemy.dialects.postgresql import UUID
import uuid


class EventStats(db.Model):
    stats_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    event_id = db.Column(UUID, db.ForeignKey('events.event_id'), nullable=False)

    views = db.Column(db.Integer, nullable=True)
    likes = db.Column(db.Integer, nullable=True)
    participants = db.Column(db.Integer, nullable=True)
    conversion = db.Column(db.Float, nullable=True)

    def as_dict(self):
        return {
            'stats_id': self.stats_id,
            'views': self.views,
            'likes': self.likes,
            'participants': self.participants,
            'conversion': self.conversion
        }
