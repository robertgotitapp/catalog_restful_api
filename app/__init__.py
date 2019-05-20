from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from app.resources.user import User
from app.security import authenticate, identity


def create_app():
    """Create and configure an instance of the Flask application"""
    from app.db import db

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://robert:robert@localhost/catalog_data'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'robert'
    api = Api(app)
    jwt = JWT(app, authenticate, identity)

    @app.before_first_request
    def create_tables():
        db.create_all()

    api.add_resource(User, '/users')
    db.init_app(app)
    return app







