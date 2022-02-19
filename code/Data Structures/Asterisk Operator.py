print(5 * 7)
print(2 ** 4)
print([0] * 10)
print([0, 1] * 10)
print((0, 1) * 10)
print("AB" * 10)
print()


numbers = [1, 2, 3, 4, 5, 6]

*beginning, last = numbers
print(beginning, last)
beginning, *last = numbers
print(beginning, last, '\n')

*beginning, middle, last = numbers
print(beginning, middle, last)
beginning, *middle, last = numbers
print(beginning, middle, last)
beginning, middle, *last = numbers
print(beginning, middle, last, '\n')

my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}
new_list = [*my_tuple, *my_list, *my_set]
print(new_list, '\n')

dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}
my_dict = {**dict_a, **dict_b}
print(my_dict)
