from flask_restful import Resource
from ..models.item import ItemModel
from ..schemas.item import ItemSchema
from flask_jwt import jwt_required, current_identity


class MyItemList(Resource):
    """
    User Resource
    """
    schema = ItemSchema()

    @staticmethod
    @jwt_required()
    def get():
        """
        Add new user to the database
        :return: newly added user data except for password
        """

        items = ItemModel.find_by_user_id(current_identity.id)
        result = []

        for item in items:
            result_item = MyItemList.schema.dump(item)
            result_item['category_name'] = item.category.name
            result_item['category_id'] = item.category.id
            result.append(result_item)

        return result, 200
