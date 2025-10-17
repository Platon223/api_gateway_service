from flask import Flask, request
from extensions.jwt import jwt


def create_service():
    app = Flask(__name__)

    jwt.init_app(app)

    @app.errorhandler(404)
    def not_found(error):
        return {'message': '404'}
    
    # register blueprints here
    from blueprints.auth.routes import gate_to_auth_bl
    app.register_blueprint(gate_to_auth_bl, url_prefix='/g/auth')

    return app
