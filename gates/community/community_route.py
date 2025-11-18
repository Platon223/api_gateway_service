from flask import request, Response
from dotenv import load_dotenv
import requests
import os

load_dotenv()

def community_route(route):
    json_data = request.get_json()
    actk_header = request.headers.get("Authorization")
    if not actk_header:
        return {"message": "no auth header provided"}
    actk = actk_header.split(" ")[1]
    req = requests.post(f"{os.getenv('COMMUNITY_SERVICE_URL')}/community/{route}", json=json_data, headers={"Authorization": f"Bearer {actk}"})

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


