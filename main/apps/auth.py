from flask import request
from functools import wraps

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']

        if not token:
            return {'message': 'Token is missing.'}, 401

        print('Token: {}'.format(token))
        return f(*args, **kwargs)

    return decorated
