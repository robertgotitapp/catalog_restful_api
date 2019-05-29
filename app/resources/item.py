from flask_restful import Resource, request
from ..models.item import ItemModel
from ..models.category import CategoryModel
from ..schemas.item import ItemSchema
from flask_jwt import jwt_required, current_identity
from ..handles.common_handles import ServerProblem, AuthorizationProblem, NotFound, BadRequest
from marshmallow import ValidationError


class Item(Resource):
    """
    Item Resource
    """
    schema = ItemSchema(partial=('id', 'created', 'updated'))

    @staticmethod
    def get(category_id, item_id):
        """
        Return item based on category_id and item_id being provided
        :param category_id: category of the item being requested
        :param item_id: item_id being requested
        :return: item corresponds to the category_id and item_id being requested
        """
        category = CategoryModel.find_by_id(category_id)
        if not category:
            raise NotFound()
        item = ItemModel.find_by_id_and_category(category_id, item_id)
        if not item:
            raise NotFound()
        return Item.schema.dump(item), 200

    @staticmethod
    @jwt_required()
    def put(category_id, item_id):
        """
        Update existing item based on category_id and item_id being provided
        :param category_id: category of the item being updated
        :param item_id: item_id of the item being updated
        :return: data of the updated item
        """
        category = CategoryModel.find_by_id(category_id)
        if not category:
            raise NotFound()
        item = ItemModel.find_by_id_and_category(category_id, item_id)
        data = request.get_json()
        try:
            Item.schema.load(data)
        except ValidationError as err:
            raise BadRequest(err.messages)
        if not item:
            raise NotFound()
        else:
            if current_identity.id != item.user_id:
                raise AuthorizationProblem()
            item.name = data['name']
            item.description = data['description']
            item.price = data['price']
            try:
                item.save_to_db()
            except Exception:
                raise ServerProblem()
            return Item.schema.dump(item), 200

    @staticmethod
    @jwt_required()
    def delete(category_id, item_id):
        """
        Delete the existing item from the database
        :param category_id: category of the item being removed
        :param item_id: id of the item being removed
        :return: successful message if the item is successfully removed
        """
        category = CategoryModel.find_by_id(category_id)
        if not category:
            raise NotFound()
        item = ItemModel.find_by_id_and_category(category_id, item_id)
        if not item:
            raise NotFound()
        if current_identity.id != item.user_id:
            raise AuthorizationProblem()
        try:
            item.delete_from_db()
        except Exception:
            raise ServerProblem()
        return {'message': 'The item has been deleted.'}
