from . import bp
from db import Redis


@bp.route('/get')
def get():
    return Redis.get('china-data')