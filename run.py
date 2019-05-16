from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from app.resources.user import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://robert:robert@localhost/catalog_data'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'robert'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(User, '/users')

if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run(port=5000, debug=True)
