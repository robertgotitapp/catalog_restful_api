from flask_restful import Resource
from ..models.category import CategoryModel
from ..schemas.category import CategorySchema
from ..handles.category import CategoryHandle


class Category(Resource):

    @staticmethod
    def get(category_id):
        category = CategoryModel.find_by_id(category_id)
        if category:
            schema = CategorySchema()
            return schema.dump(category), 200
        return CategoryHandle.handle_missing_category()
