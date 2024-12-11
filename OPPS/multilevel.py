# multi-level inheritance = when a derived(child) class inherits another derived (child) class

class Organism:
    # class variable
    alive = True
    
class Animal(Organism):
    def eat(self):
        print("This animal is Eating")

class Dog(Animal):
    def bark(self):
        print("This dog is barking")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()