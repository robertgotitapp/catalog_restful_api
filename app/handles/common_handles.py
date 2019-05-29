class _BaseErrorHandler(Exception):
    def __init__(self, message, status_code=None, payload=None):
        """
        Error Handler Constructor
        :param message: error message
        :param status_code: error status code
        :param payload: error payload
        """
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        """
        Convert error message output to dictionary
        :return: message output in the form of dictionary
        """
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


class InvalidUsage(_BaseErrorHandler):
    def __init__(self, message, status_code=None, payload=None):
        super().__init__(message, status_code, payload)


class ServerProblem(_BaseErrorHandler):
    def __init__(self):
        super().__init__('Problem occurred when server processing the action.', 500)


class AuthorizationProblem(_BaseErrorHandler):
    def __init__(self):
        super().__init__('The user is not authorized to perform this action.', 403)


class NotFound(_BaseErrorHandler):
    def __init__(self):
        super().__init__('Page Not Found.', 404)


class BadRequest(_BaseErrorHandler):
    def __init__(self, message='Bad Request'):
        super().__init__(message, 400)



