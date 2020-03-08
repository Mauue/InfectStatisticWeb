from . import bp
from db import Redis
from config import Config


@bp.route('/get')
def get():
    return Redis.get(Config.CHINA_DATA_KEY)


@bp.route('/get_province')
def get_province():
    result = b'[' + b','.join(Redis.get_list(Config.PROVINCES_DATA_KEY)) + b']'
    return result