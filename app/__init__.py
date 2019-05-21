from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from app.resources.user import User
from app.security import authenticate, identity
from app.config import config


def create_app():
    """Create and configure an instance of the Flask application"""
    from app.db import init_db

    app = Flask(__name__)
    app.config.from_object(config)
    api = Api(app)
    jwt = JWT(app, authenticate, identity)

    # @app.before_first_request
    # def create_tables():
    #     db.create_all()

    api.add_resource(User, '/users')
    init_db()
    return app







