from flask_restful import Resource, reqparse
from ..models.item import ItemModel
from ..models.category import CategoryModel
from ..schemas.item import ItemSchema
from flask_jwt import jwt_required, current_identity


class Item(Resource):
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

    @staticmethod
    def get(category_id, item_id):
        category = CategoryModel.find_by_id(category_id)
        if not category:
            return {'message': 'The item is not existed.'}, 404
        item = ItemModel.find_by_id_with_filter_by_category(category_id, item_id)
        if not item:
            return {'message': 'The item is not existed.'}, 404
        return Item.schema.dump(item).data, 200

    @staticmethod
    @jwt_required()
    def put(category_id, item_id):
        category = CategoryModel.find_by_id(category_id)
        if not category:
            return {'message': 'The item is not existed.'}, 404
        item = ItemModel.find_by_id_with_filter_by_category(category_id, item_id)
        data = Item.parser.parse_args()
        input_data = {
            'name': data['name'],
            'description': data['description'],
            'price': data['price']
        }
        messages = Item.schema.validate(input_data)
        if messages:
            return messages, 400
        if not item:
            item = ItemModel(input_data['name'],
                             input_data['description'],
                             input_data['price'],
                             category_id,
                             current_identity.id)
            try:
                item.save_to_db()
            except:
                return {'message': 'Error occurred when saving item to database.'}, 500
            return Item.schema.dump(item).data, 201
        else:
            if current_identity.id != item.user_id:
                return {'message': "The user is not authorized to perform this action."}, 403
            item.name = input_data['name']
            item.description = input_data['description']
            item.price = input_data['price']
            try:
                item.save_to_db()
            except:
                return {'message': 'Error occurred when updating item.'}, 500
            return Item.schema.dump(item).data, 200

    @staticmethod
    @jwt_required()
    def delete(category_id, item_id):
        category = CategoryModel.find_by_id(category_id)
        if not category:
            return {'message': 'The item is not existed.'}, 404
        item = ItemModel.find_by_id_with_filter_by_category(category_id, item_id)
        if not item:
            return {'message': 'The item is not existed.'}, 404
        if current_identity.id != item_id:
            return {'message': "The user is not authorized to perform this action."}, 403
        try:
            item.delete_from_db()
        except:
            {'message': 'An error occurred when deleting item.'}, 500
        return {'message': 'The item has been deleted.'}
