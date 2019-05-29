from flask_restful import Resource, request
from ..models.category import CategoryModel
from ..schemas.category import CategorySchema
from flask_jwt import jwt_required
from ..handles.common_handles import InvalidUsage, ServerProblem, BadRequest


class CategoryList(Resource):
    """
    Category List Resource
    """
    schema = CategorySchema(partial=('id', 'created', 'updated'))

    @staticmethod
    def get():
        """
        Return list of categories based on limit and offset parameters
        :return: list of up to 'limit' rows started from 'limit' category
        """
        try:
            offset = int(request.args.get('offset'))
            limit = int(request.args.get('limit'))
            results = CategoryModel.find_based_on_offset_and_limit(offset, limit)
        except Exception:
            raise InvalidUsage('Error occurred because of offset and limit parameters.', 500)
        obj = {}
        obj['total_categories'] = CategoryModel.count_rows()
        category_list = [CategoryList.schema.dump(category) for category in results]
        obj['categories'] = category_list
        return obj, 200

    @staticmethod
    @jwt_required()
    def post():
        """
        Add new category to the database
        :return: data of new category being added
        """
        data = request.get_json()
        messages = CategoryList.schema.validate(data)
        if messages:
            raise BadRequest(messages)
        category = CategoryModel(**data)

        try:
            category.save_to_db()
        except Exception:
            raise ServerProblem()

        return CategoryList.schema.dump(category), 201
