from marshmallow import Schema, fields
from ..errors.category import CategoryError


class CategorySchema(Schema):
    name = fields.Str(validate=CategoryError.validate_name)
    description = fields.Str(validate=CategoryError.validate_description)

    class Meta:
        fields = ('id',
                  'name',
                  'description',
                  'created',
                  'updated')
        ordered = True



