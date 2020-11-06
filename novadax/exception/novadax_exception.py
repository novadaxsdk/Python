class NovadaxException(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message


class RuntimeException(NovadaxException):
    pass


class RequestException(NovadaxException):
    pass
