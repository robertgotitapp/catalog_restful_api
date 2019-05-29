from .models.user import UserModel
from werkzeug.security import check_password_hash


def authenticate(username, password):
    """
    Helper function to authenticate username and password
    :param username: username being provided
    :param password: password being provided
    :return: user if username and password are correct
    """
    user = UserModel.find_by_username(username)
    if user and check_password_hash(user.password, password):
        return user


def identity(payload):
    """
    Helper function to define what is contained inside the payload of JWT
    :param payload: payload of the identity
    :return: user id of the user being authenticated at the moment
    """
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
