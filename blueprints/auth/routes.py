from flask import Flask, request, jsonify, Blueprint
from flask_jwt_extended import jwt_required
from gates.auth.auth_route import auth_route

gate_to_auth_bl = Blueprint('gate_to_auth', __name__)

@gate_to_auth_bl.route('/<endpoint>', methods=['POST', 'GET'])
def route(endpoint):
    step = request.args.get("step")
    return auth_route(f'{endpoint}' + {f'?step={step}' if step else ''})






