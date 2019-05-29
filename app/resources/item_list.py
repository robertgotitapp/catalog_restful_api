from flask_restful import Resource, request
from ..models.item import ItemModel
from ..models.category import CategoryModel
from ..schemas.item import ItemSchema
from flask_jwt import jwt_required, current_identity
from ..handles.common_handles import ServerProblem, InvalidUsage, NotFound, BadRequest
from marshmallow import ValidationError


class ItemList(Resource):
    """
    Item List Resource
    """
    schema = ItemSchema()

    @staticmethod
    @jwt_required()
    def post(category_id):
        """
        Add new item to the database
        :param category_id: category_id of the item being added
        :return: newly added item data if it is successfully added
        """
        category = CategoryModel.find_by_id(category_id)
        if not category:
            raise NotFound()

        data = request.get_json()
        try:
            ItemList.schema.load(data)
        except ValidationError as err:
            raise BadRequest(err.messages)
        item = ItemModel(data['name'],
                         data['description'],
                         data['price'],
                         category_id,
                         current_identity.id)
        try:
            item.save_to_db()
        except Exception:
            raise ServerProblem()
        return ItemList.schema.dump(item), 201

    @staticmethod
    def get(category_id):
        """
        Get list of items based on the category_id and two params offset and limit
        :param category_id: category_id of these items being requested
        :return: list of up to 'limit' items from corresponding category starting from 'offset'
        """
        category = CategoryModel.find_by_id(category_id)
        if not category:
            raise NotFound()
        try:
            offset = int(request.args.get('offset'))
            limit = int(request.args.get('limit'))
            results = ItemModel.find_based_on_offset_and_limit(offset, limit, category_id)
        except Exception:
            raise InvalidUsage('Error occurred because of offset and limit parameters.', 500)
        obj = {}
        obj['total_items'] = ItemModel.count_rows(category_id)
        schema = ItemSchema()
        item_list = [schema.dump(item) for item in results]
        obj['items'] = item_list
        return obj, 200
