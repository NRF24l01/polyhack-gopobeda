from models import db, Events
import base64
from PIL import Image
import os
import io
from config import UPLOADFLOADER
import string
import random
from flask import url_for
from werkzeug.exceptions import NotFound


def base64_to_link(base64name):
    if not base64name.startswith("data:image/"):
        raise ValueError("Некорректный формат base64 (ожидается data:image/...)")

    base64_data = base64name.split(",")[1]
    image_data = base64.b64decode(base64_data)
    image = Image.open(io.BytesIO(image_data))
    os.makedirs(UPLOADFLOADER, exist_ok=True)
    file_extension = base64name.split(";")[0].split("/")[-1]
    characters = string.ascii_letters + string.digits
    filename = ''.join(random.choices(characters, k=30))

    file_path = os.path.join(UPLOADFLOADER, f"{filename}.{file_extension}")

    if file_extension == 'gif':
        image.save(file_path, save_all=True)
    else:
        image.save(file_path)

    path = url_for('serve_image', filename=f"{filename}.{file_extension}", _external=True)

    return str(path)


def get_events_methods(query):
    query_db = db.session.query(Events)

    if query.type is not None:
        query_db = query_db.filter(Events.type == query.type)

    if query.format is not None:
        query_db = query_db.filter(Events.format == query.format)

    if query.date_from is not None:
        query_db = query_db.filter(Events.start_date >= query.date_from)

    if query.date_to is not None:
        query_db = query_db.filter(Events.end_date <= query.date_to)

    if query.status is not None:
        query_db = query_db.filter(Events.status == query.status)

    events = query_db.limit(query.limit).offset(query.offset).all()

    return events


def create_events_method(body, user_id):
    link = base64_to_link(body.image)

    new_event = Events(
        title=body.title,
        type=body.type,
        start_date=body.start_date,
        end_date=body.end_date,
        image=link,
        description=body.description,
        registration_url=body.registration_url,
        format=body.format,
        status="draft",
        user_id=user_id
    )

    if body.place is not None:
        new_event.place = body.place

    db.add(new_event)
    db.commit()

    return new_event.as_dict()


def get_event_by_event_id(event_id):
    event = Events.query.filter_by(event_id=event_id).first()
    if event is None:
        raise NotFound("Event not found")
    return event
