from flask_restplus import Namespace, Resource
from main.apps.auth import auth_required

api = Namespace('user', description='Users related operations')


@api.route('/login')
class UserLogin(Resource):
    @api.doc(security = 'apikey')
    @auth_required
    def post(self):
        return {'token':'1234567890'}
