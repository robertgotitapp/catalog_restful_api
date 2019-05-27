from flask_restful import Resource, request
from ..models.user import UserModel
from ..schemas.user import UserSchema
from ..handles.base import BaseHandle


class User(Resource):
    input_schema = UserSchema(
        only=('username', 'email', 'name', 'password'))
    output_schema = UserSchema(
        only=('id', 'username', 'email', 'name', 'created', 'updated'))

    @staticmethod
    def post():
        data = request.get_json()
        input_data = {"username": data['username'],
                      "email": data['email'],
                      "password": data['password'],
                      "name": data['name']
                      }
        messages = User.input_schema.validate(input_data)
        if messages:
            return messages, 400
        user = UserModel(input_data['username'],
                         input_data['password'],
                         input_data['name'],
                         input_data['email'])

        try:
            user.save_to_db()
        except:
            return BaseHandle.handle_server_problem()

        return User.output_schema.dump(user).data, 201
