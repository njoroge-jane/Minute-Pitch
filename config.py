import os


class Config:



    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/pitches'
#   SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}