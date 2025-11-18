from flask import Flask, request, jsonify, Blueprint
from flask_jwt_extended import jwt_required
from gates.community.community_route import community_route

gate_to_community_bl = Blueprint("gate_to_community", __name__)

@gate_to_community_bl.route('/<endpoint>', methods=["POST", "GET"])
def route(endpoint):
    return community_route(f"{endpoint}")

