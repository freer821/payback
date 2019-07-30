from ..models.user import User, Profile
from ..utils.http_helper import getresponsemsg
from flask_jwt_extended import (create_access_token)

def authenticate_user(username, password):
    user = get_user(username)
    if user and user.check_password(password):
        access_token = create_access_token(identity=username,expires_delta=False)
        return getresponsemsg(200, {'token': access_token})
    else:
        return getresponsemsg(400)


def create_user(data):
    user = User.query.filter_by(username=data['username']).first()
    if not user:
        new_user = User(
            username=data['username'],
            password=data['password'],
        )
        new_user.save()

        profile = Profile(user_id=new_user.id, full_name=data.get('full_name',''), tel=data.get('tel', ''),
                          passport=data.get('passport', ''), role=data.get('role', '0'))
        profile.save()

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

def get_profile(username):
    user = get_user(username)
    profile = Profile.query.filter_by(user_id=user.id).first()

    if profile:
        return getresponsemsg(200, profile.to_dict())
    else:
        return getresponsemsg(400, "", "user profile not found!")