
# collection = {1,2,3,4,2,3,"hello","world"}
# print(collection)
# print(type(collection))

# Empty set syntax
collection = set()

# set Method
# Add
# collection.add(1)
# collection.add(2)
# collection.add(3)
# collection.add(("luffy","time","pokemon"))
# collection.clear()
# print(len(collection))

# collection = {"hello", "pokemon", "Ash", "pikachu"}
# # Remove a random element from set
# print(collection.pop())

set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2)) # 1,2,3,4
print(set1.intersection(set2)) # 2,3