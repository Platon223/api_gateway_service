from flask import Flask, request, jsonify, Blueprint
from flask_jwt_extended import jwt_required
from gates.auth.auth_route import auth_route

gate_to_auth_bl = Blueprint('gate_to_auth', __name__)

@gate_to_auth_bl.route('/login', methods=['POST'])
def login():
    return auth_route('login?step=first_entry')

@gate_to_auth_bl.route('/register', methods=['POST'])
def register():
    return auth_route('register')

@gate_to_auth_bl.route('/verify', methods=['POST'])
def verify():
    return auth_route('verify')

@gate_to_auth_bl.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    return auth_route('refresh')






