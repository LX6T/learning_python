# Dictionary: key-value pairs, unordered, mutable

mydict = {"name": "Max", "age": 28, "city": "New York"}         # dictionary creation
print(mydict)

mydict2 = dict(name="Mary", age=27, city="Boston")              # dictionary creation
print(mydict2)

value = mydict["name"]              # access items
print(value)

mydict["email"] = "max@xyz.com"     # add items
print(mydict)

mydict["email"] = "coolmax@xyz.com"     # mutate items
print(mydict)

del mydict["name"]                  # delete items
print(mydict)

mydict.pop("age")                   # pop items
print(mydict)

mydict.popitem()                    # pop last inserted item
print(mydict)

mydict["name"] = "Max"
mydict["age"] = 28

if "name" in mydict:                    # check if key exists
    print("name: " + mydict["name"])
else:
    print("name is not in mydict")

for key in mydict:                      # iterate through keys
    print(key)

for key in mydict.keys():               # iterate through keys
    print(key)

for value in mydict.values():           # iterate through values
    print(value)

for key, value in mydict.items():       # iterate through items (key-value pairs)
    print(key, value)

mydict_cpy = mydict                     # Copy with same reference
print(mydict_cpy)
mydict_cpy["email"] = "alex@xyz.com"
print(mydict_cpy)
print(mydict)

mydict_cpy2 = mydict.copy()             # Independent copy
#            dict(mydict)
print(mydict_cpy2)
mydict_cpy2["email"] = "bob@xyz.com"
print(mydict_cpy2)
print(mydict)

mydict.update(mydict2)                  # update dictionary with another dictionary
print(mydict)



