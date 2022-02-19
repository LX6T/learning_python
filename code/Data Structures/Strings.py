# Strings: ordered, immutable, text representation

mystring = "Hello World"                # create a string
print(mystring)

mystring = """Hello
World"""                                # multiline string
print(mystring)

mystring = """Hello \
World"""                                # prevent line break
print(mystring)

char = mystring[0]                      # access items like lists
print(char)                             # strings are immutable so no modifying allowed

substring = mystring[0:8:2]             # start:stop:step
print(substring)

for i in mystring:                      # iterate over character
    print(i)

if "Wo" in mystring:                    # checks for character/substring in string
    print("Wo is in mystring")
else:
    print("Wo is not in mystring")

mystring = "        Hello     "
print(mystring)
mystring = mystring.strip()             # removes whitespace
print(mystring)

mystring = "Hello World"

print(mystring.find('o'))               # returns index of character/substring

print(mystring.count('lo'))             # returns number of characters/substrings

print(mystring.replace('World', 'Universe'))    # replace characters/substrings

mylist = mystring.split()               # string to list, default delimiter is " "
print(mylist)

newstring = " ".join(mylist)             # list to string
print(newstring)

# %

var = "Tom"
mystring = "the variable is %s" % var       # format strings
print(mystring)

var = 3
mystring = "the variable is %d" % var       # format integers
print(mystring)

var = 3.0
mystring = "the variable is %.2f" % var     # format floats
print(mystring)


# .format()

var = "Tom"
mystring = "the variable is {}".format(var)         # format strings
print(mystring)

var1, var2 = 3, 6
mystring = "the variables are {} and {}".format(var1, var2)         # format integers
print(mystring)

var = 3.0
mystring = "the variable is {:.2f}".format(var)     # format floats
print(mystring)


# fstring

var = "Tom"
mystring = f"the variable is {var}"                     # format strings
print(mystring)

var1, var2 = 3, 6
mystring = f"the variables are {var1} and {var2*2}"     # format integers
print(mystring)

var = 3.0
mystring = f"the variable is {var}"                    # format floats
print(mystring)
