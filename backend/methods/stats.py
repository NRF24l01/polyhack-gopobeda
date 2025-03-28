from models import EventStats, db


def increment_stats(event_id, type):
    stats = EventStats.query.filter_by(event_id=event_id).first()
    if stats is not None:
        if type == "likes":
            stats.likes += 1
        else:
            stats.participants += 1
    else:
        if type == "likes":
            stats = EventStats(event_id=event_id, likes=1, views=1)
        else:
            stats = EventStats(event_id=event_id, participants=1, views=1)
        db.session.add(stats)

    db.session.commit()