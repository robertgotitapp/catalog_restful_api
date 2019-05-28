from flask_restful import Resource, request
from ..models.item import ItemModel
from ..models.category import CategoryModel
from ..schemas.item import ItemSchema
from flask_jwt import jwt_required, current_identity
from ..handles.base import BaseHandle
from ..handles.item import ItemHandle


class Item(Resource):
    schema = ItemSchema(partial=('id', 'created', 'updated'))

    @staticmethod
    def get(category_id, item_id):
        category = CategoryModel.find_by_id(category_id)
        if not category:
            return ItemHandle.handle_missing_item()
        item = ItemModel.find_by_id_and_category(category_id, item_id)
        if not item:
            return ItemHandle.handle_missing_item()
        return Item.schema.dump(item), 200

    @staticmethod
    @jwt_required()
    def put(category_id, item_id):
        category = CategoryModel.find_by_id(category_id)
        if not category:
            return ItemHandle.handle_missing_item()
        item = ItemModel.find_by_id_and_category(category_id, item_id)
        data = request.get_json()
        messages = Item.schema.validate(data)
        if messages:
            return messages, 400
        if not item:
            item = ItemModel(data['name'],
                             data['description'],
                             data['price'],
                             category_id,
                             current_identity.id)
            try:
                item.save_to_db()
            except:
                return BaseHandle.handle_server_problem()
            return Item.schema.dump(item), 201
        else:
            if current_identity.id != item.user_id:
                return BaseHandle.handle_authorization_problem()
            item.name = data['name']
            item.description = data['description']
            item.price = data['price']
            try:
                item.save_to_db()
            except:
                return BaseHandle.handle_server_problem()
            return Item.schema.dump(item), 200

    @staticmethod
    @jwt_required()
    def delete(category_id, item_id):
        category = CategoryModel.find_by_id(category_id)
        if not category:
            return ItemHandle.handle_missing_item()
        item = ItemModel.find_by_id_and_category(category_id, item_id)
        if not item:
            return ItemHandle.handle_missing_item()
        if current_identity.id != item.user_id():
            return BaseHandle.handle_authorization_problem()
        try:
            item.delete_from_db()
        except:
            return BaseHandle.handle_server_problem()
        return {'message': 'The item has been deleted.'}
