from flask_restful import Resource, request
from ..models.category import CategoryModel
from ..schemas.category import CategorySchema
from flask_jwt import jwt_required
from ..handles.base import BaseHandle


class CategoryList(Resource):
    schema = CategorySchema(partial=('id', 'created', 'updated'))

    @staticmethod
    def get():
        offset = int(request.args.get('offset'))
        limit = int(request.args.get('limit'))
        results = CategoryModel.find_based_on_offset_and_limit(offset, limit)
        obj = {}
        obj['total_categories'] = CategoryModel.count_rows()
        category_list = [CategoryList.schema.dump(category) for category in results]
        obj['categories'] = category_list
        return obj, 200

    @staticmethod
    @jwt_required()
    def post():
        data = request.get_json()
        messages = CategoryList.schema.validate(data)
        if messages:
            return messages, 400
        category = CategoryModel(**data)

        try:
            category.save_to_db()
        except:
            return BaseHandle.handle_server_problem()

        return CategoryList.schema.dump(category), 201
