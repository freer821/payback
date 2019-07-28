from flask import request
from flask_restplus import Namespace, Resource
from flask_jwt_extended import (create_access_token)
api = Namespace('user', description='Users related operations')

from ..services.user import *
from ..utils.http_helper import getresponsemsg, json_required

@api.route('/login')
class UserLogin(Resource):

    @json_required
    def post(self):
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        user = get_a_user(username)
        if user and user.check_password(password):
            access_token = create_access_token(identity=username)
            return getresponsemsg(200, {'token': access_token})
        else:
            return getresponsemsg(400)
