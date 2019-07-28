from flask import Blueprint
from flask_restplus import Api

from .user import api as user_api

blueprint = Blueprint('api', __name__)

authorizations = {
    'apikey': {
        'type' : 'apiKey',
        'in'   : 'header',
        'name' : 'X-API-KEY'
    }
}


api = Api(blueprint, authorizations=authorizations, security=['apikey'])

api.add_namespace(user_api)