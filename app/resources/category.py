from flask_restful import Resource, reqparse
from ..models.category import CategoryModel
from ..schemas.category import CategorySchema


class Category(Resource):
    schema = CategorySchema(partial=('id', 'created', 'updated'))
    parser = reqparse.RequestParser()

    parser.add_argument('description',
                        type=str)

    @staticmethod
    def get(category_id):
        category = CategoryModel.find_by_id(category_id)
        if category:
            schema = CategorySchema()
            return schema.dump(category).data, 200
        return {'message': 'The category is not existed.'}, 404
