from flask import Flask
from db import init_db_command


def create_app():
    app = Flask(__name__)

    init_app(app)

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    return app


def init_app(app):
    app.cli.add_command(init_db_command)


if __name__ == '__main__':
    app = create_app()
    app.run()
