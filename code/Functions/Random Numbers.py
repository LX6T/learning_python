import random
import secrets
import numpy as np

a = random.random()             # Random float from 0 to 1
print(a)

a = random.uniform(0, 10)       # Random float from a to b
print(a)

a = random.randint(0, 10)       # Random integer from a to b (includes b)
print(a)

a = random.randrange(0, 10)     # Random integer from a to b (excludes b)
print(a)

a = random.normalvariate(0, 1)  # Random float from normal distribution mean/sd of a and b
print(a)

mylist = list("ABCDEFH")
a = random.choice(mylist)       # Random item from list
print(a)

a = random.sample(mylist, 3)    # Random sample of items from list (without replacement)
print(a)

a = random.choices(mylist, k=3)     # Random sample of items from list (without replacement)
print(a)

random.shuffle(mylist)              # Randomly shuffles a list
print(mylist)

random.seed(1)                      # Same seed leads to same pseudo-randomly generated numbers
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))
random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))


a = secrets.randbelow(10)                   # Truly random integer below n
print(a)

a = secrets.randbits(4)                     # Truly random integer below 2^n
print(a)

a = secrets.choice(mylist)                  # Truly random item from list
print(a)


a = np.random.rand(3, 3)                    # Array filled with random values from 0 to 1
print(a)

a = np.random.randint(0, 10, (3, 3))        # Array filled with random integers from 0 to 10
print(a)

np.random.shuffle(a)                        # Randomly shuffles rows
print(a)

np.random.seed(1)                           # Same seed leads to same pseudo-randomly generated numbers
print(np.random.rand(3))
np.random.seed(2)
print(np.random.rand(3))
np.random.seed(1)
print(np.random.rand(3))
np.random.seed(2)
print(np.random.rand(3))
