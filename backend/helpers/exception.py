from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException
from json import dumps

def defaultHandler(err):
    response = err.get_response()
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.get_description(),
    })
    response.content_type = 'application/json'
    return response

class ValueError(HTTPException):
    code = 400
    message = 'No message specified'
