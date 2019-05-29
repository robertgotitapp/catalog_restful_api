from marshmallow import Schema, fields
from ..validation.category import CategoryError


class CategorySchema(Schema):
    """
    Category Schema
    """
    id = fields.Integer()
    name = fields.String(
        required=True,
        error_messages={'Required': 'Name is required'},
        validate=CategoryError.validate_name
        )
    description = fields.String(validate=CategoryError.validate_description)
    created = fields.DateTime()
    updated = fields.DateTime()