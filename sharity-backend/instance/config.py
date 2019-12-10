
class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = "!24b+b31!%gy3j^!3x2ge_sirdp$=y&62hlr^96f^-_5m9j&u$"
    SQLALCHEMY_DATABASE_URI = 'postgresql://axel:Axelsharity@localhost/pruebas'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/test_db'
    DEBUG = True


class StagingConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}
