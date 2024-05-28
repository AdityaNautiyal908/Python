# WAP to check if a list contains palindrome of elements.

list = [1,2,3,2,1,]
list2 = [1,2,3,4]
copy = list.copy();
copy.reverse()

copy2 = list2.copy()
copy2.reverse()

if(copy==list):
    print("It's a palindrome list")

else:
    print("Not a palindrome list")
