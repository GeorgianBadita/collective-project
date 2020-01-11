class MyException(Exception):
    def __init__(self, errors):
        self.__errors = errors

    def get_errors(self):
        return self.__errors
