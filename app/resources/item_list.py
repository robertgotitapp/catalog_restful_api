from flask_restful import Resource, request
from ..models.item import ItemModel
from ..models.category import CategoryModel
from ..schemas.item import ItemSchema
from flask_jwt import jwt_required, current_identity
from ..handles.base import BaseHandle
from ..handles.item import ItemHandle


class ItemList(Resource):
    schema = ItemSchema(partial=('id', 'created', 'updated'))

    @staticmethod
    @jwt_required()
    def post(category_id):
        category = CategoryModel.find_by_id(category_id)
        if not category:
            return ItemHandle.handle_missing_item()

        data = request.get_json()
        input_data = {
            'name': data['name'],
            'description': data['description'],
            'price': data['price']
        }
        messages = ItemList.schema.validate(input_data)
        if messages:
            return messages, 400

        item = ItemModel(input_data['name'],
                         input_data['description'],
                         input_data['price'],
                         category_id,
                         current_identity.id)

        try:
            item.save_to_db()
        except:
            return BaseHandle.handle_server_problem()
        return ItemList.schema.dump(item).data, 201

    @staticmethod
    def get(category_id):
        category = CategoryModel.find_by_id(category_id)
        if not category:
            return ItemHandle.handle_missing_item()
        offset = int(request.args.get('offset'))
        limit = int(request.args.get('limit'))
        results = ItemModel.find_based_on_offset_and_limit(offset, limit, category_id)
        obj = {}
        obj['total_items'] = ItemModel.count_rows()
        schema = ItemSchema()
        item_list = [schema.dump(item).data for item in results]
        obj['items'] = item_list
        return obj, 200
