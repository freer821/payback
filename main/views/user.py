from flask import request
from flask_restplus import Namespace, Resource
from flask_jwt_extended import (jwt_required,get_jwt_identity)
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
        return create_user(username, password)


@api.route('/profile')
class UserProfile(Resource):

    @json_required
    @jwt_required
    def post(self):
        username = get_jwt_identity()
        return update_user_profile(username, request.json)

    @jwt_required
    def get(self):
        username = get_jwt_identity()
        return get_profile(username)