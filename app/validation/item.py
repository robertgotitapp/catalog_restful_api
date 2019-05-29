from marshmallow import ValidationError


class ItemError:

    @staticmethod
    def validate_name(name):
        if len(name) > 40:
            raise ValidationError('Name length must be equal or shorter than 40 characters.')
        elif len(name) < 5:
            raise ValidationError('Name length must be at least 5 characters.')

    @staticmethod
    def validate_description(description):
        if len(description) > 200:
            raise ValidationError('Description length must be equal or lower than 200 characters.')

    @staticmethod
    def validate_price(price):
        if price < 0:
            raise ValidationError('Price cannot be negative number.')
