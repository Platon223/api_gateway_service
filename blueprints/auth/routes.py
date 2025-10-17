from flask import Flask, request, jsonify, Blueprint
from flask_jwt_extended import jwt_required
from gates.auth_login import login

gate_to_auth_bl = Blueprint('gate_to_auth', __name__)

@gate_to_auth_bl.route('/login', methods=['POST'])
def login():
    login()




