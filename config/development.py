from .base import BaseConfig

class DevelopmentConfig(BaseConfig):
    DATABASE_URI = 'mysql+mysqlconnector://robert:robert@localhost/catalog_data'
    DEBUG = True