
class Config:
    REDIS_HOST = 'localhost'
    REDIS_PORT = '6379'
    REDIS_DB = 0
    REDIS_PREFIX = 'ISW:'

    REDIS_URL = 'redis://{}:{}/{}'.format(REDIS_HOST, REDIS_PORT, REDIS_DB)

    CHINA_DATA_KEY = "china-data"
    PROVINCES_DATA_KEY = "provinces-data"
    TREND_DATA_KEY = 'trend-data'
    INDEX_PAGE_DATA_KEY = "index-data"

    JOBS = [
        {
            'id': 'job3',
            'func': 'util.crawler:set_all_data_task',
            'args': '',
            'trigger': {
                'type': 'interval',
                'seconds': 21600  # 6个小时更新一次
            }
        },
    ]
