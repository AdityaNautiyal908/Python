# capitals = {"India" : "New Delhi",
#             "China" : "Beijing",
#             "Russia" : "Moscow"}


# 1. get = To get the particular value at that key
# 2. pop = To pop the key and value 
# 3. popitem = To pop the last inserted value at Dictionary
# 4. clear = To remove all the key and value from the Dictionary
# 5. keys = To get the keys at the Dictionary
# 6. values = To get the values at the Dictionary
# 7. update = To insert more value to Dictionary or update a value
# 8. items = To get both the key and value from the Dictionary


# Concession stand program

menu = {"pizza" : 65,
        "nachos" : 70,
        "popcorn" : 90,
        "fries" : 50,
        "chips" : 20,
        "pretzel" : 40,
        "soda" : 20,
        "lemonade" : 20}

cart = []
total = 0
running = True

print("----------- MENU -----------")
for key, value in menu.items():
    print(f"{key:10} : ₹{value:.2f}")
print("----------------------------")

while running:
    food = input("Select an item (q to quit) : ")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------------- YOUR ORDER ---------------")
for food in cart:
    total += menu.get(food)    
    print(food,end=" ")

print()
print(f"Total is : ₹{total:.2f}")

