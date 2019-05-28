from flask_restful import Resource, request
from ..models.user import UserModel
from ..schemas.user import UserSchema
from ..handles.base import BaseHandle
from marshmallow import ValidationError


class User(Resource):
    schema = UserSchema()

    @staticmethod
    def post():
        data = request.get_json()
        try:
            User.schema.load(data)
        except ValidationError as err:
            errors = err.messages
            return errors

        user = UserModel(**data)

        try:
            user.save_to_db()
        except:
            return BaseHandle.handle_server_problem()

        return User.schema.dump(user), 201
