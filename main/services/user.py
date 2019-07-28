from ..models.user import User, Profile
from ..utils.http_helper import getresponsemsg
from flask_jwt_extended import (create_access_token)

def authenticate_user(username, password):
    user = get_user(username)
    if user and user.check_password(password):
        access_token = create_access_token(identity=username)
        return getresponsemsg(200, {'token': access_token})
    else:
        return getresponsemsg(400)


def create_user(username, password):
    user = User.query.filter_by(username=username).first()
    if not user:
        new_user = User(
            username=username,
            password=password,
        )
        new_user.save()

        return getresponsemsg(200, 'Successfully registered.')
    else:
        return getresponsemsg(409, 'User already exists.')


def get_users():
    return User.query.all()


def get_user(username):
    return User.query.filter_by(username=username).first()


def update_user_profile(username, data):
    user = get_user(username)
    profile = Profile.query.filter_by(user_id=user.id).first()
    if profile:
        profile.name = data.get('name','')
        profile.address= data.get('address', '')
        profile.passport_no=data.get('passport_no', '')
        profile.update()
    else:
        profile = Profile(user_id=user.id, name=data.get('name',''), address=data.get('address', ''), passport_no=data.get('passport_no', ''))
        profile.save()

    return getresponsemsg(200, "update Successfully!")
