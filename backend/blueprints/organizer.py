from flask import Blueprint, jsonify
from helpers import *
from methods import *
from models import EventStats
from werkzeug.exceptions import BadRequest
from flask_pydantic import validate
from schemas import *

organizer = Blueprint('organizer', __name__)


@organizer.route("events/drafts", methods=['GET'])
@creates_response
@jwt_required()
@check_jwt_access
@validate()
def get_drafts(query: QueryRequest):
    events = get_events_methods(query)
    events = [event.as_dict() for event in events]

    return jsonify(events), 200


@organizer.route('/events', methods=['GET'])
@creates_response
@jwt_required()
@check_jwt_access
def get_organizer_events():
    uuid = get_jwt_identity()
    events = Events.query.filter(Events.user_id == uuid).all()
    events = [event.as_dict() for event in events]

    return jsonify(events), 200


@organizer.route('/events/{event_id}/stats', methods=['GET'])
@creates_response
@jwt_required()
@check_jwt_access
def get_organizer_event_stats(event_id):
    uuid = get_jwt_identity()
    event = EventStats.query.filter_by(user_id=uuid, event_id=event_id).first()
    if event is None:
        raise BadRequest('Event not found')

    return jsonify(event.as_dict()), 200
