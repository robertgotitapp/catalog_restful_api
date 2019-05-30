from marshmallow import ValidationError


class ItemError:

    @staticmethod
    def validate_name(name):
        """
        Validate if name is between 5 and 40 characters length
        :param name: name being checked
        :return: raise the ValidationError if any condition is violated
        """
        if len(name) > 40:
            raise ValidationError('Name length must be equal or shorter than 40 characters.')
        elif len(name) < 5:
            raise ValidationError('Name length must be at least 5 characters.')

    @staticmethod
    def validate_description(description):
        """
        Validate if description is within 200 characters length
        :param description: description being checked
        :return: raise the ValidationError if any condition is violated
        """
        if len(description) > 200:
            raise ValidationError('Description length must be equal or lower than 200 characters.')

    @staticmethod
    def validate_price(price):
        """
        Validate if price is a positive float
        :param price: price being checked
        :return: raise the ValidationError if any condition is violated
        """
        if price < 0:
            raise ValidationError('Price cannot be negative number.')
