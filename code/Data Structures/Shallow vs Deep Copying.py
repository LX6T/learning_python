org = 5
cpy = org                   # not a copy, org and cpy have same reference
cpy = 6                     # rebinds cpy to a different value, doesn't affect org
print('', org, cpy)

org = [0, 1, 2, 3, 4]
cpy = org                   # not a copy, org and cpy have same reference
cpy[0] = -10                # both org and cpy are changed
print('', org, '\n', cpy)


import copy

# shallow copy: one level deep, only references of nested child objects
# deep copy: full independent copy

org = [[0, 1, 2], [3, 4, 5]]
cpy = copy.copy(org)        # shallow copy
# cpy = org.copy()
# cpy = list(org)
# cpy = org[:]
cpy[0][0] = 9
print('', org, '\n', cpy)

org = [[0, 1, 2], [3, 4, 5]]
cpy = copy.deepcopy(org)        # deep copy
cpy[0][0] = 9
print('', org, '\n', cpy, '\n')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee


p1 = Person('Alex', 27)
p2 = p1                     # not a copy
p2.age = 28
print(p1.age, p2.age)

p1 = Person('Alex', 27)
p2 = copy.copy(p1)          # shallow copy
p2.age = 28
print(p1.age, p2.age)

p1 = Person('Alex', 27)
p2 = Person('Joe', 20)
company = Company(p1, p2)
company_clone = copy.copy(company)          # shallow copy
company_clone.boss.age = 28
print(company.boss.age, company_clone.boss.age)

p1 = Person('Alex', 27)
p2 = Person('Joe', 20)
company = Company(p1, p2)
company_clone = copy.deepcopy(company)      # deep copy
company_clone.boss.age = 28
print(company.boss.age, company_clone.boss.age)



