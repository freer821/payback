from flask import request, jsonify, make_response
from functools import wraps

def getresponsemsg(status, msg='', err=''):
    # 200 - 300 for sucess
    # 400 ~ for error
    # 500 ~ for system error
    return make_response(jsonify({
        'msg': msg,
        'err': err
    }), status)

def json_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not request.is_json:
            return getresponsemsg(400, '', 'json required!')

        return f(*args, **kwargs)

    return decorated