from abc import ABC, abstractmethod


class Animal(ABC): # inherit from ABC
    @abstractmethod # decorator to define an abstract method
    def feed(self):
        pass

# class Panda(Animal): # If a class inherits from an ABC, it must implement all it's abstract methods!
#     def wrong_name(self): # The method's name must match the name of the ABC's method
#         print("Feeding a panda with some tasty bamboo!")

# <ipython-input-77-11c744dfb979> in <module>
# ----> 1 po = Panda()

# TypeError: Can't instantiate abstract class Panda with abstract methods feed

# In [78]: 

class Lion(Animal):
    def feed(self):
        print("Feeding a lion with raw meat!")

class Panda(Animal):
    def feed(self):
        print("Feeding a panda with tasty bamboo!")


class Snake(Animal):
    def feed(self):
        print("Feeding a snake with mice")

zoo = [Lion(), Panda(), Snake()]

for animal in zoo:
    animal.feed()