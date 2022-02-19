# Tuple: ordered, immutable, allows duplicate elements

mytuple = ("Max", 28, "Boston")
# mytuple = tuple(["Max", 28, "Boston"])
print(mytuple)

minituple = ("Max")
print(type(minituple))
minituple = ("Max",)    # Needs a comma to be recognised as a tuple
print(type(minituple))

print("mytuple[0]: " + mytuple[0])
print("mytuple[-1]: " + mytuple[-1])

try:
    mytuple[0] = "Dave"             # tuples are immutable
except TypeError:
    print("TypeError: 'tuple' object does not support item assignment")

for i in mytuple:
    print(i)

print("banana" in mytuple)

mytuple = tuple("apple")            # convert string to tuple
print(mytuple)
print("len(mytuple): " + str(len(mytuple)))                 # length of tuple
print("mytuple.count('p'): " + str(mytuple.count('p')))     # count characters
print("mytuple.index('p'): " + str(mytuple.index('p')))     # index of first character occurrence

a = mytuple[1:4:1]                  # start:stop:step
print(a)

i1, *i2, i3 = mytuple               # first, everything in between, last
print(i1)
print(i2)
print(i3)

mytuple = "Max", 28, "Boston"

name, age, city = mytuple
print(name)
print(age)
print(city)

import sys
mylist = [0, 1, 2, "hello", True]
mytuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(mylist), "bytes")
print(sys.getsizeof(mytuple), "bytes")  # Tuples use less memory than lists

import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))     # Tuples are faster to create than lists


