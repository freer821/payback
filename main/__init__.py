from flask import Flask
from main.views import blueprint as api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
flask_bcrypt = Bcrypt()

def create_app(config_dict):
    app = Flask(__name__)
    app.config.from_object(config_dict)
    app.register_blueprint(api, url_prefix='/api/v1')

    db.init_app(app)
    flask_bcrypt.init_app(app)

    return app
