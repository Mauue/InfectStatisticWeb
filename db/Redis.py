import redis
from config import REDIS_PRIFIX, REDIS_PORT, REDIS_HOST


class _Redis:
    def __init__(self):
        self.conn = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=1)
        self.conn.ping()

        self._prefix = REDIS_PRIFIX


    def get(self, key):
        return self.conn.get(self._prefix + key)

    def set(self, key, value, ex=None, px=None, nx=None, xx=None):
        self.conn.set(self._prefix + key, value, ex, px, nx, xx)

