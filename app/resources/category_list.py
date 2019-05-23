from flask_restful import Resource, request, reqparse
from ..models.category import CategoryModel
from ..schemas.category import CategorySchema
from flask_jwt import jwt_required


class CategoryList(Resource):
    schema = CategorySchema(partial=('id', 'created', 'updated'))
    parser = reqparse.RequestParser()

    parser.add_argument('name',
                        type=str,
                        required=True,
                        help='This field cannot be blank.')

    parser.add_argument('description',
                        type=str)

    @staticmethod
    def get():
        offset = int(request.args.get('offset'))
        limit = int(request.args.get('limit'))
        results = CategoryModel.find_based_on_offset_and_limit(offset, limit)
        obj = {}
        obj['total_categories'] = CategoryModel.count_rows()
        category_list = [CategoryList.schema.dump(category).data for category in results]
        obj['categories'] = category_list
        return obj, 200

    @staticmethod
    @jwt_required()
    def post():
        data = CategoryList.parser.parse_args()
        input_data = {
            'name': data['name'],
            'description': data['description']
        }
        messages = CategoryList.schema.validate(input_data)
        if messages:
            return messages, 400
        category = CategoryModel(input_data['name'],
                                 input_data['description'])

        try:
            category.save_to_db()
        except:
            return {'message': 'Error occurred when saving category to database.'}, 500

        return CategoryList.schema.dump(category).data, 201