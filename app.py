from flask import Flask, current_app
from api import bp as api_bp
from flask_apscheduler import APScheduler
from config import Config
from util.crawler import set_all_data_task
import db
import logging

scheduler = APScheduler()


def create_app():
    _app = Flask(__name__)
    _app.config.from_object(Config)

    init_app(_app)

    scheduler.init_app(_app)
    scheduler.start()

    set_all_data_task()  # 运行前先获取一次数据

    return _app


def init_app(app):
    app.register_blueprint(api_bp)
