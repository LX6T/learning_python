def print_name(name):       # parameter
    print(name)


print_name('Alex\n')          # argument


def foo(a, b, c, d=4):      # default parameter value (must be at the end)
    print(a, b, c, d)


foo(1, 2, 3)                # positional arguments
foo(c=2, a=3, b=1)          # keyword arguments
foo(1, b=1, c=3)            # mix of both
# foo(1, b=1, 3)            # positional after keyword raises error
# foo(1, b=1, a=3)          # a = 1 and 3, raises error
foo(1, 2, 3, 5)             # override default argument
print()


def bar(a, b, *args, **kwargs):     # variable length arguments and keyword arguments
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])


bar(1, 2, 3, 4, 5, six=6, seven=7)
print()


def fee(a, b, *, c, d):      # forces c and d to be keyword arguments
    print(a, b, c, d)


fee(1, 2, c=3, d=4)
print()


def bee(*args, last):
    for arg in args:
        print(arg)
    print('last:', last)


bee(1, 2, 3, last=100)    # last must be a keyword argument


