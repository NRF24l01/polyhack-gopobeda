from flask import Blueprint, jsonify
from helpers import *
from methods import *
from flask_pydantic import validate
from schemas import *

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