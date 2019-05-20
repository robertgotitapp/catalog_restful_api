from .base import BaseConfig

class TestingConfig(BaseConfig):
    DATABASE_URI = 'mysql+mysqlconnector://robert:robert@localhost/test_catalog_data'
    TESTING = True
    DEBUG = True


