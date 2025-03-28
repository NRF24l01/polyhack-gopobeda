from flask import Blueprint, jsonify
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


@events.route("", methods=['POST'])
@creates_response
@jwt_required()
@check_jwt_access
@validate()
def create_events(body: CreateEventsRequest):
    events = create_events_method(body)

    return jsonify(events), 201
