from marshmallow import ValidationError
from ..models.user import UserModel
import re


class UserError:

    @staticmethod
    def validate_username(username):
        """
        Validate if username is between 5 and 30 characters length, and if the username has been used
        :param username: username being checked
        :return: raise the ValidationError if any condition is violated
        """
        if len(username) > 30:
            raise ValidationError('Username length must be equal or shorter than 30 characters.')
        elif len(username) < 5:
            raise ValidationError('Name length must be at least 5 characters.')
        elif UserModel.find_by_username(username):
            raise ValidationError('The username has been taken.')

    @staticmethod
    def validate_name(name):
        """
        Validate if name is within 40 characters length
        :param name: name being checked
        :return: raise the ValidationError if any condition is violated
        """
        if len(name) > 40:
            raise ValidationError('Name length must be equal or shorter than 40 characters.')

    @staticmethod
    def validate_email(email):
        """
        Validate if email has been registered with another account
        :param email: email being checked
        :return: raise the ValidationError if any condition is violated
        """
        if UserModel.find_by_email(email):
            raise ValidationError('The email has been registered with another account.')


    @staticmethod
    def validate_password(password):
        """
        Validate if password is longer than 8 characters, includes at least on letter and one number
        :param password: password being checked
        :return: raise the ValidationError if any condition is violated
        """
        if len(password) < 8:
            raise ValidationError('Password must be longer than 8 characters.')
        elif not re.match("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", password):
            raise ValidationError('Password has to have the length of more than 8 characters, at least'
                                  'one letter and one number.')
