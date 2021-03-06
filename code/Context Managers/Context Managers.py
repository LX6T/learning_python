from contextlib import contextmanager

# without using a context manager:
file = open('notes.txt', 'w')
try:
    file.write('some todo...')
finally:
    file.close()

# using a context manager:
with open('notes.txt', 'w') as file:
    file.write('some todo...')


# implement context manager as a class
class ManagedFile:
    def __init__(self, filename):
        print('init')
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('exception has been handled')
        # print('exc:', exc_type, exc_value)
        print('exit')
        return True


with ManagedFile('notes.txt') as file:
    print('do some stuff')
    file.write('some todo...')
    file.somemethod()
print('continuing')


# implement context manager as a function
@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()


with open_managed_file('notes.txt') as f:
    f.write('some todo...')
