# https://realpython.com/python3-object-oriented-programming/

class Dog:
    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print('bark!!')
    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")
        
# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def bark(self):
        print('barks loudly!')
        
dog = Dog('fluffy pug', 3)
print (dog)
dog.bark()
dog.doginfo()

RussellTerrier('pino', 5).bark()

print(isinstance(dog, RussellTerrier))
