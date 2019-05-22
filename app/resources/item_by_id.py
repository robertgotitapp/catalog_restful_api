from flask_restful import Resource, reqparse
from ..models.item import ItemModel
from ..models.category import CategoryModel
from ..schemas.item import ItemSchema
from flask_jwt import jwt_required, current_identity


class ItemById(Resource):
    schema = ItemSchema(partial=('id', 'created', 'updated'))
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="this field cannot be blank.")
    parser.add_argument('description',
                        type=str,
                        required=True,
                        help="this field cannot be blank.")
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="this field cannot be blank.")

    def get(self, category_name, item_id):
        category = CategoryModel.find_by_name(category_name)
        if not category:
            return {'message': 'The category is not existed.'}, 404
        item = ItemModel.find_by_id_with_filter_by_category(category.id, item_id)
        if not item:
            return {'message': 'The item is not existed.'}, 404
        return ItemById.schema.dump(item), 200

    @jwt_required()
    def put(self, category_name, item_id):
        category = CategoryModel.find_by_name(category_name)
        if not category:
            return {'message': 'The category is not existed.'}, 404
        item = ItemModel.find_by_id_with_filter_by_category(category.id, item_id)
        data = ItemById.parser.parse_args()
        input_data = {
            'name': data['name'],
            'description': data['description'],
            'price': data['price']
        }
        messages = ItemById.schema.validate(input_data)
        if messages:
            return messages, 400
        if not item:
            item = ItemModel(input_data['name'],
                             input_data['description'],
                             input_data['price'],
                             category.id,
                             current_identity.id)
            try:
                item.save_to_db()
            except:
                return {'message': 'Error occurred when saving item to database.'}, 500
            return ItemById.schema.dump(item), 201
        else:
            if current_identity.id != item_id:
                return {'message': "The user is not authorized to perform this action."}, 403
            item.name = input_data['name']
            item.description = input_data['description']
            item.price = input_data['price']
            try:
                item.save_to_db()
            except:
                return {'message': 'Error occurred when updating item.'}, 500
            return ItemById.schema.dump(item), 200

    @jwt_required()
    def delete(self, category_name, item_id):
        category = CategoryModel.find_by_name(category_name)
        if not category:
            return {'message': 'The category is not existed.'}, 404
        item = ItemModel.find_by_id_with_filter_by_category(category.id, item_id)
        if not item:
            return {'message': 'The item is not existed.'}, 404
        if current_identity.id != item_id:
            return {'message': "The user is not authorized to perform this action."}, 403
        try:
            item.delete_from_db()
        except:
            {'message': 'An error occurred when deleting item.'}, 500
