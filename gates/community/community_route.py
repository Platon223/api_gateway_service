from flask import request
from dotenv import load_dotenv
import requests
import os

load_dotenv()

def community_route(route):
    requests.post(f"{os.getenv("COMMUNITY_SERVICE_URL")}/community/{route}")
    

