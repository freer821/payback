from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
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
