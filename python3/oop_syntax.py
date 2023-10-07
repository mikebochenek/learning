# https://realpython.com/python3-object-oriented-programming/
class Dog:
    def __init__(self, name, age): # Initializer / Instance Attributes
        self.name = name
        self.age = age
    def bark(self):
        print('bark!!')
    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")
        
class RussellTerrier(Dog): # Child class (inherits from Dog class)
    def bark(self):
        print('barks loudly!')
        
dog = Dog('fluffy pug', 3)
print ('default string representation:', dog)
dog.bark()
dog.doginfo()

rt = RussellTerrier('pino', 5)
rt.bark()
print('is dog a russelterrier?', isinstance(dog, RussellTerrier))
print('is russelterrier a dog?', isinstance(rt, Dog))
