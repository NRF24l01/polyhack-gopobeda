from . import db, Users
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Events(db.Model):
    __tablename__ = 'events'

    event_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    title = db.Column(db.String(300), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Integer, nullable=False)
    end_date = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(500))
    description = db.Column(db.Text)
    registration_url = db.Column(db.String(600))

    format = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)

    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey(Users.user_id, ondelete="CASCADE"))
    organizer = db.relationship('Users', foreign_keys=[user_id], backref='events')

    liked = db.relationship("EventLiked", backref="event", uselist=True)
    participating = db.relationship("EventParticipating", backref="event", uselist=True)
    stats = db.relationship("EventStats", backref="event", uselist=False)

    def as_dict(self):
        return {
            'event_id': self.event_id,
            'title': self.title,
            'type': self.type,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'image_url': self.image_url,
            'description': self.description,
            'registration_url': self.registration_url,
            "format": self.format,
            "status": self.status,
            "organizer": self.organizer.as_dict(),

        }
