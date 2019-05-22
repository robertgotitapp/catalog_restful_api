from flask_restful import Resource, request
from ..models.category import CategoryModel
from ..schemas.category import CategorySchema


class CategoryList(Resource):
    schema = CategorySchema(partial=('id', 'created', 'updated'))

    def get(self):
        offset = int(request.args.get('offset'))
        limit = int(request.args.get('limit'))
        results = CategoryModel.find_based_on_offset_and_limit(offset, limit)
        obj = {}
        obj['total_categories'] = CategoryModel.count_rows()
        category_list = [CategoryList.schema.dump(category) for category in results]
        obj['categories'] = category_list
        return obj, 200
