from flask_restplus import Namespace, Resource, fields

api = Namespace('users', description='Users related operations')

user = api.model('User', {
    'id': fields.String(required=True, description='The user identifier'),
    'name': fields.String(required=True, description='The user name'),
})

USERS = [
    {'id': 'felix', 'name': 'Felix'},
]

@api.route('/sign-in')
class UserLogin(Resource):
    @api.doc('user_login')
    def post(self):
        return {'token':'1234567890'}
