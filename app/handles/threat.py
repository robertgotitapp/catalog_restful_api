class _BaseErrorHandler(Exception):
    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


class InvalidUsage(_BaseErrorHandler):
    def __init__(self, message, status_code=None, payload=None):
        super.__init__(message, status_code, payload)
