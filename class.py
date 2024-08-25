class Mammal:
    def walk(self):
        print(f"walk")

class Dog(Mammal):
    pass

class Cat(Mammal):
    pass

dog = Dog()
dog.walk()
