import redis
from config import REDIS_PREFIX, REDIS_PORT, REDIS_HOST


class _Redis:
    def __init__(self):
        self.conn = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=1)
        self.conn.ping()

        self._prefix = REDIS_PREFIX

    def get(self, name):
        return self.conn.get(self._prefix + name)

    def set(self, name, value, ex=None, px=None, nx=None, xx=None):
        self.conn.set(self._prefix + name, value, ex, px, nx, xx)

    def lpush(self, name, *values):
        self.conn.lpush(self._prefix + name, *values)

    def rpush(self, name, *values):
        self.conn.rpush(self._prefix + name, *values)

    def clear_list(self, name):
        self.conn.ltrim(self._prefix + name, 1, 0)

    def get_list(self, name):
        return self.conn.lrange(self._prefix + name, 0, -1)

