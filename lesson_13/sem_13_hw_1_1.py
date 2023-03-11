class UserException(Exception):
    pass


class ValueTypeError(UserException):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Value input should have integer type. Entered type is {type(self.value)}"


class DequeLengthError(UserException):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Deque length cannot be less than zero. Entered length is {self.value}"
