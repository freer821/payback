from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from sqlalchemy import MetaData

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
flask_bcrypt = Bcrypt()

from main.views import blueprint, api

def create_app(config_dict):
    app = Flask(__name__)
    app.config.from_object(config_dict)
    app.register_blueprint(blueprint, url_prefix='/api/v1')

    jwt = JWTManager(app)
    jwt._set_error_handler_callbacks(api)

    db.init_app(app)
    flask_bcrypt.init_app(app)

    return app
