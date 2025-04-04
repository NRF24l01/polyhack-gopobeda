from flask import Blueprint, jsonify
from helpers import *
from methods import *
from flask_pydantic import validate
from schemas import *
from models import EventLiked, EventParticipating, EventStats

user = Blueprint('user', __name__)


@user.route("/events/saved", methods=['GET'])
@creates_response
@jwt_required()
@validate()
def get_saved(query: QueryRequest):
    user = get_jwt_identity()
    events = get_events_methods(query)
    res = []
    for event in events:
        if event.liked.user_id == user:
            res.append(event.as_dict())

    return jsonify(res), 200


@user.route("/events/participating", methods=['GET'])
@creates_response
@jwt_required()
@validate()
def get_participating(query: QueryRequest):
    user = get_jwt_identity()
    events = get_events_methods(query)
    res = []
    for event in events:
        if event.participating.user_id == user:
            res.append(event.as_dict())

    return jsonify(res), 200


@user.route("/events/{event_id}/like", methods=['POST'])
@creates_response
@jwt_required()
def like_for_event(event_id):
    user_id = get_jwt_identity()
    event_id = get_event_by_event_id(event_id)

    like = EventLiked(user_id=user_id, event_id=event_id)
    db.session.add(like)

    increment_stats(event_id, "likes")

    db.session.commit()

    return jsonify({"details": "ok"}), 200


@user.route("/events/{event_id}/participating", methods=['POST'])
@creates_response
@jwt_required()
def participating_for_event(event_id):
    user_id = get_jwt_identity()
    event_id = get_event_by_event_id(event_id)

    participating = EventParticipating(user_id=user_id, event_id=event_id)
    db.session.add(participating)

    increment_stats(event_id, "participating")

    db.session.commit()

    return jsonify({"details": "ok"}), 200
