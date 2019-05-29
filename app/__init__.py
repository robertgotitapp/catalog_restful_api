from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT
from app.resources.user import User
from app.resources.category_list import CategoryList
from app.resources.category import Category
from app.resources.item import Item
from app.resources.item_list import ItemList
from app.security import authenticate, identity
from app.config import config
from app.handles.common_handles import BadRequest, NotFound, _BaseErrorHandler


def create_app():
    # Create and configure an instance of the Flask application
    from app.db import init_db

    app = Flask(__name__)

    app.config.from_object(config)
    api = Api(app)

    # Calling JWT will define the /auth endpoint for authentication
    JWT(app, authenticate, identity)

    # End points definition
    api.add_resource(User, '/users')
    api.add_resource(CategoryList, '/categories')
    api.add_resource(Category, '/categories/<int:category_id>')
    api.add_resource(ItemList, '/categories/<int:category_id>/items')
    api.add_resource(Item, '/categories/<int:category_id>/items/<int:item_id>')
    init_db()

    # Errors handles registration
    @app.errorhandler(404)
    def page_not_found():
        raise NotFound()

    @app.errorhandler(400)
    def bad_request():
        raise BadRequest()

    @app.errorhandler(_BaseErrorHandler)
    def handle_error(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    return app
