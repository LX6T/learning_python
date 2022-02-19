# Sets: unordered, mutable, no duplicates

myset = {1, 2, 3, 1, 2}         # set creation
print(myset)

myset = set([1, 2, 3])          # list to set
print(myset)

myset = set("Hello")            # string to set
print(myset)

myset = set()                   # create empty set

myset.add(1)                    # add items to set
myset.add(2)
myset.add(3)

myset.remove(1)                 # remove items
myset.discard(2)                # remove items if they exist
myset.clear()                   # remove all items

myset = {1, 2, 3}
print(myset.pop())              # pop items
print(myset)

for i in myset:                 # iterate over items
    print(i)

if 2 in myset:                  # check existence
    print("yes")

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)           # union of two sets
print(u)

i = odds.intersection(primes)   # intersection of two sets
print(i)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)    # difference of two sets A \ B
print(diff)

diff = setA.symmetric_difference(setB)    # symmetric difference of two sets (A \ B) + (B \ A)
print(diff)

setA.update(setB)               # updates set with another set
print(setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}      # intersection update
setA.intersection_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}      # difference update
setA.difference_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.symmetric_difference_update(setB)  # symmetric intersection update
print(setA)

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setC = {7, 8}

print(setA.issubset(setB))              # is A a subset of B
print(setB.issubset(setA))              # is B a subset of A

print(setA.issuperset(setB))            # is A a superset of B
print(setB.issuperset(setA))            # is B a superset of A

print(setA.isdisjoint(setB))            # is A disjoint with B
print(setA.isdisjoint(setC))            # is A disjoint with C

setB = setA                             # copy reference
setB.add(7)
print(setB)
print(setA)

setB = setA.copy()                      # new copy
#      set(setA)
setB.add(8)
print(setB)
print(setA)

a = frozenset([1, 2, 3, 4])             # create a frozenset
print(a)
a.add(5)                                # frozensets are immutable
