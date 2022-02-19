# lambda arguments: expression

add10 = lambda x: x + 10        # adds 10 to a number
print(add10(5))

mult = lambda x, y: x * y       # multiply two numbers
print(mult(2, 7))

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])       # sorts by sum of x and y
print(points2D)
print(points2D_sorted)


# map(func, seq)

a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)       # b = a*2
print(list(b))
c = [x*2 for x in a]            # Same result with list comprehension
print(c)


# filter(func, seq)

a = [1, 2, 3, 4, 5]
b = filter(lambda x: x % 2 == 0, a)         # Filters away odd numbers
print(list(b))
c = [x for x in a if x % 2 == 0]
print(c)                                    # Same result with list comprehension


# reduce(func, seq)

from functools import reduce

a = [1, 2, 3, 4, 5]
b = reduce(lambda x, y: x * y, a)         # Multiplies all the numbers together
print(b)
