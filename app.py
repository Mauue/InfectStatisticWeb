import json

from flask import Flask, request
from flask_apscheduler import APScheduler
from config import Config
from util.crawler import set_all_data_task
from util.schedule import ScheduleConfig
from db import Redis
import logging

scheduler = APScheduler()


def create_app():
    _app = Flask(__name__)
    _app.config.from_object(Config)
    _app.config.from_object(ScheduleConfig)

    init_app(_app)

    scheduler.init_app(_app)
    scheduler.start()

    set_all_data_task()  # 运行前先获取一次数据

    @_app.route('/api/index')
    def get_index():
        return Redis.get(Config.INDEX_PAGE_DATA_KEY)

    @_app.route('/api/news')
    def get_news():
        return Redis.get(Config.NEWS_DATA_KEY)

    @_app.route('/api/province')
    def get_province():
        province = request.args.get('name')
        data = Redis.get(province) if province else ''
        return data if data else ''

    return _app


def init_app(app):
    pass
