from flask_restful import Resource, request
from ..models.user import UserModel
from ..models.item import ItemModel
from ..schemas.user import UserSchema
from ..schemas.item import ItemSchema
from marshmallow import ValidationError
from ..handles.common_handles import ServerProblem, BadRequest
from flask_jwt import jwt_required, current_identity


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
            print(err.messages)
            raise BadRequest(err.messages)
        user = UserModel(**data)
        try:
            user.save_to_db()
        except Exception:
            raise ServerProblem()
        return User.schema.dump(user), 201

    @staticmethod
    @jwt_required()
    def get():
        itemSchema = ItemSchema()
        user_id = current_identity.id
        user = UserModel.find_by_id(user_id)
        obj = {}
        obj['user'] = User.schema.dump(user)
        items = ItemModel.find_by_user_id(user_id)
        item_list = [itemSchema.dump(item) for item in items]
        obj['items'] = item_list
        return obj, 200




