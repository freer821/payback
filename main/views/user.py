from flask import request
from flask_restplus import Namespace, Resource

api = Namespace('user', description='Users related operations')

from ..services.user import *
from ..utils.http_helper import json_required

@api.route('/login')
class UserLogin(Resource):

    @json_required
    def post(self):
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        return authenticate_user(username, password)


@api.route('/signup')
class UserSignup(Resource):

    @json_required
    def post(self):
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        return create_new_user(username, password)