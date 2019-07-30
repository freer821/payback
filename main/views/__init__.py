from flask import Blueprint
from flask_restplus import Api

from .user import api as user_api
from .shop import api as shop_api

blueprint = Blueprint('api', __name__)
api = Api(blueprint)
api.add_namespace(user_api)
api.add_namespace(shop_api)