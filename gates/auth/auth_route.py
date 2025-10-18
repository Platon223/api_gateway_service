from flask import request, Response
from dotenv import load_dotenv
import os
import requests

load_dotenv()

def auth_route(service_route):
    json_data = request.get_json()
    req = requests.post(f"{os.getenv('AUTH_SERVICE_URL')}/auth/{service_route}", json=json_data)

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
    


