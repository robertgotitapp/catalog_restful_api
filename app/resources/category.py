from flask_restful import Resource
from ..models.category import CategoryModel
from ..schemas.category import CategorySchema
from ..handles.common_handles import NotFound


class Category(Resource):
    """
    Category Resource
    """

    @staticmethod
    def get(category_id):
        """
        Return category data based on category_id
        :param category_id: category_id being requested
        :return: category data corresponds to the requested category_id
        """
        category = CategoryModel.find_by_id(category_id)
        if category:
            schema = CategorySchema()
            return schema.dump(category), 200
        raise NotFound()
