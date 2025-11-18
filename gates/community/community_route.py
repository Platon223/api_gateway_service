from flask import request, Response
from dotenv import load_dotenv
import requests
import os

load_dotenv()

def community_route(route):
    json_data = request.get_json()
    req = requests.post(f"{os.getenv("COMMUNITY_SERVICE_URL")}/community/{route}", json=json_data)

    if req.status_code == 200:
        return Response(
            req.text,
            status=req.status_code,
            content_type=req.headers.get("content-type")
        )
    else:
        return Response(
            req.text,
            status=req.status_code
        )


