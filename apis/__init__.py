from flask import Blueprint
from flask_restplus import Api

from .user import api as user
blueprint = Blueprint('api', __name__)

api = Api(blueprint)

api.add_namespace(user)