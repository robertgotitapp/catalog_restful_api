from flask_restful import Resource
from ..models.category import CategoryModel
from ..schemas.category import CategorySchema


class IndividualCategory(Resource):

    def get(self, id):
        category = CategoryModel.find_by_id(id)
        if category:
            schema = CategorySchema()
            return schema.dump(category), 200
        return {'message': 'The category is not existed.'}, 404



