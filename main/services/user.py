from ..models.user import User
from ..utils.http_helper import getresponsemsg
from flask_jwt_extended import (create_access_token)

def authenticate_user(username, password):
    user = get_a_user(username)
    if user and user.check_password(password):
        access_token = create_access_token(identity=username)
        return getresponsemsg(200, {'token': access_token})
    else:
        return getresponsemsg(400)


def create_new_user(username, password):
    user = User.query.filter_by(username=username).first()
    if not user:
        new_user = User(
            username=username,
            password=password,
        )
        new_user.save_to_db()

        return getresponsemsg(200, 'Successfully registered.')
    else:
        return getresponsemsg(409, 'User already exists.')


def get_all_users():
    return User.query.all()


def get_a_user(username):
    return User.query.filter_by(username=username).first()