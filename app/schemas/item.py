from marshmallow import Schema, fields
from ..errors.item import ItemError


class ItemSchema(Schema):
    id = fields.Integer()
    name = fields.String(
        required=True,
        error_messages={'Required': 'Name is required'},
        validate=ItemError.validate_name)
    description = fields.String(
        validate=ItemError.validate_description)
    price = fields.Float(
        required=True,
        error_messages={'Required': 'Price is required'},
        validate=ItemError.validate_price)
    created = fields.DateTime()
    updated = fields.DateTime()
