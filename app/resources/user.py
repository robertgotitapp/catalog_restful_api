from flask_restful import Resource, reqparse
from ..models.user import UserModel
from ..schemas.user import UserSchema
from werkzeug.security import generate_password_hash


class User(Resource):
    schema = UserSchema(only=(
        'id', 'username', 'email', 'name', 'created', 'updated'
    ), partial=('id', 'created', 'updated')
    )
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank.")

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank.")

    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be blank.")

    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="This field cannot be blank.")
    def post(self):
        data = User.parser.parse_args()
        input_data = {"username": data['username'],
                      "email": data['email'],
                      "password": data['password'],
                      "name": data['name']
                      }
        messages = User.schema.validate(input_data)
        if messages:
            return messages, 400
        hashed_password = generate_password_hash(data['password'], method='sha256')
        user = UserModel(input_data['username'],
                         hashed_password,
                         input_data['name'],
                         input_data['email'])

        try:
            user.save_to_db()
        except:
            return {'message': 'Error occurred when saving data to database.'}

        return User.schema.dump(user), 201
