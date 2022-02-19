def foo(a, b, c):
    print(a, b, c)


my_list = [0, 1, 2]         # can also be a tuple
foo(*my_list)

my_dict = {'a': 1, 'b': 2, 'c': 3}      # keys must match parameters
foo(**my_dict)


def bar():
    global number                       # can use variables from outside function
    x = number
    number = 3
    print('number inside function:', x)


number = 0
bar()
print(number)


def fee(x):
    x = 5


var = 10
fee(var)
print(var)                              # immutable objects are unaffected by changes within methods


def bee(a_list):
    # a_list = [100, 200, 300]          # rebinding stops outer object from being changed
    a_list.append(4)
    # a_list += [100, 200, 300]             # doesn't rebind reference, [1, 2, 3, 4, 100, 200, 300]
    # a_list = a_list + [100, 200, 300]     # rebinds reference, [1, 2, 3, 4]


my_list = [1, 2, 3]
bee(my_list)
print(my_list)                          # mutable objects are unaffected by changes within methods
