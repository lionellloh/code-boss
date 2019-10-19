import os

class Config(object):
    """
    Common configurations
    """
    JWT_SECRET_KEY = "thisisnottherealsecretkeydumbass"
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = "refresh"

    # Number of seconds it takes for expiry. 24 hours.
    JWT_ACCESS_TOKEN_EXPIRES = 86400

class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'p9Bv<3Eid9%$i01'
    # MONGO_URI = "mongodb://localhost:27017/50043db"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/codebossdb'




class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False
    # MONGO_URI = "mongodb://mongodb:27017/50043db"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@mysqldb/50043db'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://favebook_admin:password@mysqldb/50043db'

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}