import os


class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = "key"
    SECURITY_PASSWORD_SALT = "security-password-salt"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = "development"
    SERVER_NAME = "127.0.0.1:5000"
    PAGINATE_PAGE_SIZE = 5
