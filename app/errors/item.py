from marshmallow import ValidationError


class ItemError:

    @staticmethod
    def validate_name(name):
        if len(name) > 40:
            raise ValidationError('Name length must be equal or lower than 40.')

    @staticmethod
    def validate_description(description):
        if len(description) > 200:
            raise ValidationError('Description length must be equal or lower than 200 characters.')
