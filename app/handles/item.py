class ItemHandle:
    @staticmethod
    def handle_missing_item():
        return {'message': 'The item is not existed.'}, 404