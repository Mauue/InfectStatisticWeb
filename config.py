
class Config:
    REDIS_HOST = 'localhost'
    REDIS_PORT = '6379'
    REDIS_PASSWORD = None
    REDIS_DB = 0
    REDIS_PREFIX = 'ISW:'

    REDIS_URL = 'redis://{}:{}/{}'.format(REDIS_HOST, REDIS_PORT, REDIS_DB)

    INDEX_PAGE_DATA_KEY = "index-data"
    NEWS_DATA_KEY = "news-data"

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
