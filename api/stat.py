from . import bp
from db import Redis
from config import Config


@bp.route('/index')
def get():
    return Redis.get(Config.INDEX_PAGE_DATA_KEY)


