from .. import flask_bcrypt
from .base import db, Base
from ..utils.com_helper import getRandomNo
class User(Base):
    """ User Model for storing user related details """
    __tablename__ = "user"

    username = db.Column(db.String(255), unique=True, nullable=False)
    _password = db.Column(db.String(100))
    profile = db.relationship("Profile", uselist=False, backref="user")
    is_superuser = db.Column.(db.Boolean())

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self._password = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self._password, password)


class Profile(Base):
    __tablename__ = "user_profile"

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_no = db.Column(db.String(50), unique=True, nullable=False, default=getRandomNo)
    full_name = db.Column(db.String(50), default="")
    tel = db.Column(db.String(50), default="")
    address = db.Column(db.String(200), default="")
    passport = db.Column(db.String(50), default="")
    role = db.Column(db.String(30), default="")
