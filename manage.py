from flask import Flask
from apis import blueprint as api

from config import config_by_name


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.register_blueprint(api, url_prefix='/api/v1')

    return app


if __name__ == '__main__':
    app = create_app('dev')
    app.run(host='0.0.0.0', use_reloader=True,debug=True)
