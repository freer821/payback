import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """basic config"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A0Zr98j/3yXR~XHH!jmN]LWX/,?RT'
    # SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True

    # send mail
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_ASCII_ATTACHMENTS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = '2399447849'
    MAIL_PASSWORD = ''
    FLASKY_MAIL_SUBJECT_PREFIX = u'DevOps Flask RestPlus API'
    FLASKY_MAIL_SENDER = '2399447849@qq.com'
    FLASKY_ADMIN = '2399447849@qq.com'


class Development(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'payback_dev.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(Config):
    DEBUG = False


config_by_name = {
    'dev': Development,
    'production': Production,
}
