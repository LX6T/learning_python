# Itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

from itertools import product
a = [1, 2]
b = [3]
prod = product(a, b, repeat=2)      # Product of two lists (set multiplication); repeat = squared, cubed, etc.
print(list(prod))


from itertools import permutations
a = [1, 2, 3]
perm = permutations(a, 2)           # Permutations
print(list(perm))


from itertools import combinations, combinations_with_replacement
a = [1, 2, 3, 4]
comb = combinations(a, 2)                       # Combinations without replacement
print(list(comb))
comb_wr = combinations_with_replacement(a,2)    # Combinations with replacement
print(list(comb_wr))


from itertools import accumulate
import operator
a = [1, 2, 3, 4]
acc = accumulate(a, func=operator.mul)      # Accumulates list items, default operator is +
print(list(acc))


from itertools import groupby

a = [1, 2, 3, 4]
group_obj_1 = groupby(a, key=lambda x: x < 3)       # Groups items by key
for key, value in group_obj_1:
    print(key, list(value))

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]
group_obj_2 = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj_2:
    print(key, list(value))


from itertools import count, cycle, repeat

for i in count(10):         # Counts infinitely starting from 10
    print(i)
    if i == 15:
        break

a = [1, 2, 3]
b = 0
for i in cycle(a):          # Cycles infinitely through list
    print(i)
    b += 1
    if b == 10:
        break

for i in repeat(10, 4):     # Repeats finitely or infinitely
    print(i)
