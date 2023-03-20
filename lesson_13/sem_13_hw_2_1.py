class UserException(Exception):
    pass


class LengthTypeError(UserException):

    def __init__(self, length):
        self.value = length

    def __str__(self):
        return f"Length should be integer or float. Entered value has type {type(self.value)}"


class WidthTypeError(UserException):

    def __init__(self, width):
        self.value = width

    def __str__(self):
        return f"Width should be integer or float. Entered value has type {type(self.value)}"


class LengthValueError(UserException):

    def __init__(self, length):
        self.length = length

    def __str__(self):
        return f"Length value cannot be less than or equal to zero. Entered length is {self.length}"


class WidthValueError(UserException):

    def __init__(self, width):
        self.width = width

    def __str__(self):
        return f"Width value cannot be less than or equal to zero. Entered width is {self.width}"
