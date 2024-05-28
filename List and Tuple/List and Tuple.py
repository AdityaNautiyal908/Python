# list in python 
# Just like other language we have array , In python we have list which can also store different list element in it
# list is mutable in python
# But string is immutable in python


# marks = [10,60,68,89,20,20]

# List Methods

# adds one element at end
# marks.append(10)

# Reverse list
# marks.reverse()

# insert element at index
# marks.insert(2,40)

# sort in ascending order
# marks.sort()

# sort in descending order
# marks.sort(reverse=True)

# Remove first occurrence of element
# marks.remove(20)

# Remove element at index
# marks.pop(3)

# print(marks)

# Tuples in Python
# A built-in data type that lets us create immutable sequence of values.

# list = (1,2,3,4,5)

# print(list)
# print(type(list))

# Empty tuple

# tup = ()
# print(tup)

# tup = (1,)
# print(tup)

# Tuple Method
tup = (1,2,3,4,2,2)

# Return index of first occurrence 
print(tup.index(2))

# Count Total occurrence
print(tup.count(2))
