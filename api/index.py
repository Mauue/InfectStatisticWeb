from . import bp
from db import Redis
from config import CHINA_DATA_KEY, PROVINCES_DATA_KEY


@bp.route('/get')
def get():
    return Redis.get(CHINA_DATA_KEY)


@bp.route('/get_province')
def get_province():
    result = b'[' + b','.join(Redis.get_list(PROVINCES_DATA_KEY)) + b']'
    return result