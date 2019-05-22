from flask_restful import Resource, reqparse
from ..models.item import ItemModel
from ..models.category import CategoryModel
from ..schemas.item import ItemSchema
from flask_jwt import jwt_required, current_identity


class Item(Resource):
    schema = ItemSchema(partial=('id', 'created', 'updated'))
    parser = reqparse.RequestParser()
    parser.add_argument('description',
                        type=str)
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="this field cannot be blank.")

    @jwt_required()
    def post(self, category_name, item_name):
        category = CategoryModel.find_by_name(category_name)
        if not category:
            return {'message': 'Category not found'}, 404

        data = Item.parser.parse_args()
        input_data = {
            'name': item_name,
            'description': data['description'],
            'price': data['price']
        }
        messages = Item.schema.validate(input_data)
        if messages:
            return messages, 400

        item = ItemModel(input_data['name'],
                         input_data['description'],
                         input_data['price'],
                         category.id,
                         current_identity.id)

        try:
            item.save_to_db()
        except:
            return {'message': 'Error occurred when saving item to database.'}, 500
        return Item.schema.dump(item), 201

    # How to implement this, still implement find item_name, but also implement find item_by_id end point
    def get(self, category_name, item_name):
        category = CategoryModel.find_by_name(category_name)
        if not category:
            return {'message': 'The category is not existed.'}, 404
        items = ItemModel.find_by_name(category.id, item_name)
        if not items:
            return {'message': 'The item is not existed.'}, 404
        item_list = [Item.schema.dump(item) for item in items]
        return item_list, 200
