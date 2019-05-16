from marshmallow import Schema, fields, post_load
from ..models.user import UserModel
from ..errors.user import UserError


class UserSchema(Schema):
    id = fields.Integer()
    username = fields.Str(validate=UserError.validate_username)
    email = fields.Email(validate=UserError.validate_email)
    name = fields.Str(validate=UserError.validate_name)
    password = fields.Str(validate=UserError.validate_password)

    class Meta:
        fields = ('id',
                  'username',
                  'email',
                  'name',
                  'password',
                  'created',
                  'updated')
        ordered = True

    @post_load
    def make_user(self, data):
        return UserModel(**data)




