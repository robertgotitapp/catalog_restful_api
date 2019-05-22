from flask_restful import Resource, reqparse
from ..models.item import ItemModel
from ..models.category import CategoryModel
from ..schemas.item import ItemSchema
from flask_jwt import jwt_required, current_identity


class ItemById(Resource):
    schema = ItemSchema(partial=('name', 'description', 'price', 'id', 'created', 'updated'))
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str)
    parser.add_argument('description',
                        type=str)
    parser.add_argument('price',
                        type=float)

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
        if not item:
            return {'message': 'The item is not existed.'}, 404
        if current_identity.id != item_id:
            return {'message': "The user is not authorized to perform this action."}, 403
        data = ItemById.parser.parse_args()
        pass


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

