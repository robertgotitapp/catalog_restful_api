from flask_restful import Resource, reqparse, request
from ..models.category import CategoryModel
from ..schemas.category import CategorySchema
from flask_jwt import jwt_required


class Category(Resource):
    schema = CategorySchema(partial=('id', 'created', 'updated'))
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="this field cannot be blank.")

    parser.add_argument('description',
                        type=str)

    @jwt_required
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
            return {'message': 'Error occurred when saving data to database.'}, 500

        return Category.schema.dump(category), 201


    def get(self):
        offset = int(request.args.get('offset'))
        limit = int(request.args.get('limit'))
        print(limit, offset)
        results = CategoryModel.query.all()
        count = len(results)
        if count < offset:
            return {'message': 'Categories not found because of offset being set too high'}, 404
        obj = {}
        categories_list = []
        obj['total_categories'] = count
        end_index = min(count, offset + limit)
        for index in range(offset, end_index):
            categories_list.append(Category.schema.dump(results[index]))
        obj['categories'] = categories_list
        return obj, 200


