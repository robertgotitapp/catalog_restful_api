from .base import _Config


class _TestConfig(_Config):
    DATABASE_URI = 'mysql+mysqlconnector://robert:robert@localhost/test_catalog_restful_api'
    DEBUG = True


config = _TestConfig
