from models import db, Events


def get_events_methods(query):
    query_db = db.session.query(Events)

    if query.type is not None:
        query_db = query_db.filter(Events.type == query.type)

    if query.format is not None:
        query_db = query_db.filter(Events.format == query.format)

    if query.dateFrom is not None:
        query_db = query_db.filter(Events.start_date >= query.dateFrom)

    if query.dateTo is not None:
        query_db = query_db.filter(Events.end_date <= query.dateTo)

    events = query_db.limit(query.limit).offset(query.offset).all()
    events = [event.as_dict() for event in events]

    return events


def create_events_method(body):
    new_event = Events(
        title=body.title,
        type=body.type,
        start_date=body.start_date,
        end_date=body.end_date,
        image=body.image,
        description=body.description,
        registration_url=body.registration_url,
        format=body.format,
        status=body.status
    )

    db.add(new_event)
    db.commit()

    return new_event.as_dict()
