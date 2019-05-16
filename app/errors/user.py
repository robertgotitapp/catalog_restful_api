from marshmallow import ValidationError
from ..models.user import UserModel


class UserError:

    @staticmethod
    def validate_username(username):
        if len(username) > 30:
            raise ValidationError('Username length must be equal or lower than 30.')
        elif UserModel.find_by_username(username):
            raise ValidationError('The username has been taken.')

    @staticmethod
    def validate_name(name):
        if len(name) > 40:
            raise ValidationError('Name length must be equal or lower than 40.')

    @staticmethod
    def validate_email(email):
        if UserModel.find_by_email(email):
            raise ValidationError('The email has been registered with another account.')

    @staticmethod
    def validate_password(password):
        pass
