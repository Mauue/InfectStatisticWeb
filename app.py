from flask import Flask
from api import bp as api_bp
import db


def create_app():
    _app = Flask(__name__)

    init_app(_app)

    @_app.route('/')
    def hello_world():
        return 'Hello World!'

    return _app


def init_app(app):
    app.register_blueprint(api_bp)


if __name__ == '__main__':
    app = create_app()
    app.run()
