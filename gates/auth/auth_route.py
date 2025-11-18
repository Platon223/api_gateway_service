from flask import request, Response
from dotenv import load_dotenv
import os
import requests

load_dotenv()

def auth_route(service_route):
    if service_route != 'refresh':

        json_data = request.get_json()
        req = requests.post(f"{os.getenv('AUTH_SERVICE_URL')}/auth/{service_route}", json=json_data)
    else:
        actk_header = request.headers.get('Authorization')
        if not actk_header:
            return {"message": "no auth header provided"}
        actk = actk_header.split(" ")[1]
        req = requests.post(f"{os.getenv('AUTH_SERVICE_URL')}/auth/{service_route}", headers={'Authorization': f'Bearer {actk}'})

    if req.status_code == 200:
        return Response(
            req.text,
            status=req.status_code,
            content_type=req.headers.get('content-type')
        )
    else:
        return Response(
            req.text,
            status=req.status_code
        )
    


