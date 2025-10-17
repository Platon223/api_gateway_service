from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()


def create_service():
    app = Flask(__name__)

    @app.errorhandler(404)
    def not_found(error):
        return {'message': '404'}
    
    # register blueprints here


    return app
