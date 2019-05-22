from marshmallow import Schema, fields
from ..errors.item import ItemError


class ItemSchema(Schema):
    name = fields.Str(validate=ItemError.validate_name)
    description = fields.Str(validate=ItemError.validate_description)
    price = fields.Float(validate=ItemError.validate_price)

    class Meta:
        fields = ('id',
                  'name',
                  'description',
                  'price',
                  'user_id',
                  'category_id',
                  'created',
                  'updated')
        ordered = True



