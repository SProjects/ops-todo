import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '6678509e124efe369846ee550463ee080154b91e343e7260db52a45d8b747f8f24624149692191a7'


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY') or Config.SECRET_KEY
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or None


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'postgresql://localhost/todo_dev'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/todo_test'


configuration = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    staging=StagingConfig
)
