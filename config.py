

class BasicConfig(object):
    BASIC_AUTH_USERNAME = 'gabi'
    BASIC_AUTH_PASSWORD = 'baietas'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

    SECRET_KEY = ''

    TEMPLATES_AUTO_RELOAD = True

    PASSWORD_SALT = ''

    # EMAIL SETTINGS
    MAIL_SERVER = ''
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    MAIL_DEFAULT_SENDER = ''
