import sys


def mygenerator():
    yield 1
    yield 2
    yield 3


def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1


def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


g = mygenerator()

# for i in g:
#     print(i)

for _ in range(4):
    try:
        print(next(g))
    except StopIteration:
        print("StopIteration")

g = mygenerator()
print(f"sum = {sum(g)}")


cd = countdown(4)

for _ in range(5):
    try:
        print(next(cd))
    except StopIteration:
        print("StopIteration")


print(sum(firstn(10)))
print(sum(firstn_generator(10)))

print(sys.getsizeof(firstn(100000)))
print(sys.getsizeof(firstn_generator(100000)))


fib = fibonacci(30)
for i in fib:
    print(i)

mygenerator = (i for i in range(10) if i % 2 == 0)
for i in mygenerator:
    print(i)
print(list(mygenerator))
print(sys.getsizeof(mygenerator))

mylist = [i for i in range(10) if i % 2 == 0]
print(mylist)
print(sys.getsizeof(mylist))
