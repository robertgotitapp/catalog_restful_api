from flask_restful import Resource
from ..models.category import CategoryModel
from ..schemas.category import CategorySchema
from ..handles.category import CategoryHandle


class Category(Resource):
    schema = CategorySchema(partial=('id', 'created', 'updated'))

    @staticmethod
    def get(category_id):
        category = CategoryModel.find_by_id(category_id)
        if category:
            schema = CategorySchema()
            return schema.dump(category).data, 200
        return CategoryHandle.handle_missing_category()
