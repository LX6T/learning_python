# List: ordered, mutable, allows duplicate elements

mylist = ["banana", "cherry", "apple"]  # Creates a list
print(mylist)

print("mylist[0]: " + mylist[0])
print("mylist[-1]: " + mylist[-1])

for i in mylist:                    # Iterates over list items
    print(i)

print("banana" in mylist)           # Checks for item in list

mylist.append("lemon")              # Appends item to end of list
print(mylist)
print("len(mylist): " + str(len(mylist)))

mylist.insert(1, "blueberry")       # Inserts item at position 1
print(mylist)

item = mylist.pop()                 # Returns last item and deletes it
print("Popper item: " + item)
print(mylist)

mylist.remove("cherry")             # Removes specified item
print("Removed cherry")
print(mylist)

# mylist.clear() clears the list

mylist.sort()                       # Sorts the list alphanumerically
print("Sorted")
print(mylist)

mylist.reverse()                    # Reverses the list
print("Reversed")
print(mylist)

newlist = sorted(mylist)            # Copy of sorted list
print(mylist)
print(newlist)


mylist = [0, 1] * 2                 # Repeated elements
print(mylist)

newlist = mylist + [1, 2, 3, 4, 5]  # Concatenation
print(newlist)

a = newlist[1:7:2]                  # start:stop:step
print(a)

mylistcpy = mylist                  # Copy with the same reference
mylistcpy.append(6)
print(mylistcpy)
print(mylist)

mylistcpy = mylist.copy()           # Independent copy
#           list(mylist)
#           mylist[:]
mylistcpy.append(7)
print(mylistcpy)
print(mylist)

mylist = [1, 2, 3, 4, 5, 6]
newlist = [i*i for i in mylist]     # List comprehension
print(mylist)
print(newlist)

