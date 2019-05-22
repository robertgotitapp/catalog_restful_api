from marshmallow import ValidationError
from ..models.item import ItemModel


class ItemError:

    @staticmethod
    def validate_name(name):
        pass

    @staticmethod
    def validate_description(description):
        pass

    @staticmethod
    def validate_price(price):
        pass
