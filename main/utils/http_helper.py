from flask import request, jsonify
from functools import wraps

def getresponsemsg(status, msg='', err=''):
    return jsonify({
        'status': status,
        'msg': msg,
        'err': err
    })

def json_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not request.is_json:
            return getresponsemsg(400, '', 'json required!')

        return f(*args, **kwargs)

    return decorated