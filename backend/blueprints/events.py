from flask import Blueprint, jsonify, request
from schemas import *
from methods import *
from helpers import *
from flask_pydantic import validate
from flask_jwt_extended import jwt_required

events = Blueprint('events', __name__)


@events.route("", methods=['GET'])
@creates_response
@validate()
def get_events(query: QueryRequest):
    events = get_events_methods(query)
    events = [event.as_dict() for event in events]
    return jsonify(events), 200


@events.route("/{events_id}", methods=['GET'])
@creates_response
def get_events_by_event_id(events_id):
    event = get_event_by_event_id(events_id)

    return jsonify(event.as_dict()), 200


@events.route("", methods=['POST'])
@creates_response
@jwt_required()
@check_jwt_access
@validate()
def create_events(body: CreateEventsRequest):
    user_id = get_jwt_identity()
    print(body)
    events = create_events_method(body, user_id)

    return jsonify(events), 201


@events.route("/pull/from/json", methods=['POST'])
@creates_response
@jwt_required()
@is_admin
def pull_db_from_json():
    body = request.get_json()
    user_id = get_jwt_identity()
    events = create_events_from_json(body, user_id)

    return jsonify(events), 201
