class BaseHandle:
    @staticmethod
    def handle_server_problem():
        return {'message': 'Error occurred when handling action.'}, 500

    @staticmethod
    def handle_authorization_problem():
        return {'message': "The user is not authorized to perform this action."}, 403
