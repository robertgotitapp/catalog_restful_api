from flask_restful import Resource, reqparse
from ..models.category import CategoryModel
from ..schemas.category import CategorySchema
from flask_jwt import jwt_required


class Category(Resource):
    schema = CategorySchema(partial=('id', 'created', 'updated'))
    parser = reqparse.RequestParser()

    parser.add_argument('description',
                        type=str)

    @jwt_required()
    def post(self, category_name):
        data = Category.parser.parse_args()
        input_data = {
            'name': category_name,
            'description': data['description']
        }
        messages = Category.schema.validate(input_data)
        if messages:
            return messages, 400
        category = CategoryModel(input_data['name'],
                                 input_data['description'])

        try:
            category.save_to_db()
        except:
            return {'message': 'Error occurred when saving category to database.'}, 500

        return Category.schema.dump(category), 201

    def get(self, category_name):
        category = CategoryModel.find_by_name(category_name)
        if category:
            schema = CategorySchema()
            return schema.dump(category), 200
        return {'message': 'The category is not existed.'}, 404


