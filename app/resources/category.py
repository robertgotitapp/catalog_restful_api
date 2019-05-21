from flask_restful import Resource, reqparse
from ..models.category import CategoryModel
from ..schemas.category import CategorySchema


class Category(Resource):
    schema = CategorySchema(partial=('id', 'created', 'updated'))
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="this field cannot be blank.")

    parser.add_argument('description',
                        type=str)

    def post(self):
        data = Category.parser.parse_args()
        input_data = {
            'name': data['name'],
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
            return {'message': 'Error occurred when saving data to database.'}

        return Category.schema.dump(category), 201

    def get(self):
        return [Category.schema.dump(category) for category in CategoryModel.query.all()]


