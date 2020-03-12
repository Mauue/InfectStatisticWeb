
class Config:

    # 可修改项
    REDIS_HOST = 'localhost'
    REDIS_PORT = '6379'
    REDIS_PASSWORD = None
    REDIS_DB = 0
    REDIS_PREFIX = 'ISW:'

    # 建议不修改项
    INDEX_PAGE_DATA_KEY = "index-data"
    NEWS_DATA_KEY = "news-data"
    REDIS_URL = 'redis://{}:{}/{}'.format(REDIS_HOST, REDIS_PORT, REDIS_DB)