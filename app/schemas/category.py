from marshmallow import Schema, fields
from ..errors.category import CategoryError


class CategorySchema(Schema):
    name = fields.Str(validate=CategoryError.validate_name)
    description = fields.Str(validate=CategoryError.validate_description)
    created = fields.DateTime()
    updated = fields.DateTime()

    class Meta:
        fields = (
                  'name',
                  'description',
                  'created',
                  'updated')
        ordered = True
