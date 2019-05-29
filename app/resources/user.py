from flask_restful import Resource, request
from ..models.user import UserModel
from ..schemas.user import UserSchema
from marshmallow import ValidationError
from ..handles.common_handles import ServerProblem, BadRequest


class User(Resource):
    """
    User Resource
    """
    schema = UserSchema()

    @staticmethod
    def post():
        """
        Add new user to the database
        :return: newly added user data except for password
        """
        data = request.get_json()
        try:
            User.schema.load(data)
        except ValidationError as err:
            raise BadRequest(err.messages)
        user = UserModel(**data)
        try:
            user.save_to_db()
        except Exception:
            raise ServerProblem()
        return User.schema.dump(user), 201
