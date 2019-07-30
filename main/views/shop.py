from flask import request
from flask_restplus import Namespace, Resource
from flask_jwt_extended import (jwt_required,get_jwt_identity)
api = Namespace('shop', description='shop related operations')

from ..services.shop import *
from ..utils.http_helper import json_required

@api.route('/list')
class Shop(Resource):

    @jwt_required
    def get(self):
        return get_shop_list()