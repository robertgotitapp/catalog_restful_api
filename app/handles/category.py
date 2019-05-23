class CategoryHandle:
    @staticmethod
    def handle_missing_category():
        return {'message': 'The category is not existed.'}, 404
