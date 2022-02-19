import functools


def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")                      # Do something before
        result = func(*args, **kwargs)      # Function call
        print("End")                        # Do something after
        return result                       # Return
    return wrapper


def repeat(num_times):
    def decorator_repeat(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper


class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)


@start_end_decorator
def add5(x):
    return x + 5


result = add5(10)
print(result)
print(help(add5))
print(add5.__name__)

print('\n')


@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")


greet("Alex")

print('\n')


@debug
@start_end_decorator
def say_hello(name):
    greeting = f"Hello {name}"
    print(greeting)
    return greeting


say_hello("Alex")

print('\n')


@CountCalls
def hello():
    print("Hello")


hello()
hello()
hello()


