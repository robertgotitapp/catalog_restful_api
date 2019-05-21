from marshmallow import ValidationError
from ..models.user import UserModel
import re


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

    # This does not get to run
    @staticmethod
    def validate_password(password):
        if len(password) < 8:
            raise ValidationError('Password must be longer than 8 characters.')
        elif not re.match("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", password):
            raise ValidationError('Password has to have the length of more than 8 characters, at least'
                                  'one letter and one number.')
