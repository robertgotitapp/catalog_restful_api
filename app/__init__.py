from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from app.resources.user import User
from app.resources.category_list import CategoryList
from app.resources.category import Category
from app.resources.item import Item
from app.resources.item_list import ItemList
from app.security import authenticate, identity
from app.config import config


def create_app():
    """Create and configure an instance of the Flask application"""
    from app.db import init_db

    app = Flask(__name__)

    app.config.from_object(config)
    api = Api(app)

    JWT(app, authenticate, identity)

    api.add_resource(User, '/users')
    api.add_resource(CategoryList, '/categories')
    api.add_resource(Category, '/categories/<int:category_id>')
    api.add_resource(ItemList, '/categories/<int:category_id>/items')
    api.add_resource(Item, '/categories/<int:category_id>/items/<int:item_id>')
    init_db()
    return app
