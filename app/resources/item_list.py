from flask_restful import Resource, request
from ..models.item import ItemModel
from ..models.category import CategoryModel
from ..schemas.item import ItemSchema


class ItemList(Resource):

    def get(self, category_name):
        offset = int(request.args.get('offset'))
        limit = int(request.args.get('limit'))
        category_id = CategoryModel.find_by_name(category_name).id
        results = ItemModel.find_based_on_offset_and_limit(offset, limit, category_id)
        obj = {}
        obj['total_items'] = ItemModel.count_rows()
        schema = ItemSchema()
        item_list = [schema.dump(item) for item in results]
        obj['items'] = item_list
        return obj, 200

