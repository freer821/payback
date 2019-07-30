from .. import flask_bcrypt
from .base import db, Base

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

    def __repr__(self):
        return "<User '{}'>".format(self.username)


class Profile(Base):
    __tablename__ = "user_profile"

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(100), default="")
    address = db.Column(db.String(200), default="")
    passport_no = db.Column(db.String(50), default="")