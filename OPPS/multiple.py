class Organism:
    alive = True


class Bacteria:
    bread_mold = True
    

class Virus:
    kill = False


class Dog(Organism,Bacteria,Virus):
    def bark(self):
        print("Dog can bark")

dog = Dog()

print(dog.alive)
print(dog.bread_mold)
print(dog.kill)
dog.bark()