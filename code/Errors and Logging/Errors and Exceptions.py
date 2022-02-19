# Errors and Exceptions

#   SyntaxError: code is syntactically incorrect
#   TypeError: Using/mixing wrong types
#   ModuleNotFoundError: Trying to import a module that doesn't exist
#   NameError: Referencing a variable that doesn't exist
#   FileNotFoundError: Trying to access a file that doesn't exist
#   ValueError: Function receives value of correct type but inappropriate value
#   IndexError: Trying to access an index that is out of range or does not exist

x = -5

try:
    if x < 0:
        raise Exception('x should be positive')
except Exception as e:
    print(e)

try:
    assert (x >= 0), 'x is not positive'
except AssertionError as e:
    print(e)


class ValueTooHighError(Exception):
    pass


class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooLowError('value is too low:', x)


try:
    test_value(0)
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e.message, e.value)
else:
    print('everything is fine')
finally:
    print('cleaning up...')