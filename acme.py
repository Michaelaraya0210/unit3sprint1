import random
import unittest


#Create a class here

class Product:
    def __init__(self, name= "A Cool Toy"):
        self.name = name
        self.price = 10
        self.weight = 20
        self.flammability = 0.5
        self.identifier = random.randint(999999, 9999999)

    def stealability(self):
        stealratio = self.price / self.weight
        if stealratio < .05:
          return print("Not so stealable..")
        if stealratio >= .05 and stealratio < 1.0:
          return print('Kinda stealable...')
        else:
           print('very stealable')

    def explode(self):
        hotratio = self.weight * self.flammability
        if hotratio < 10:
            return print("...fizzle")
        if hotratio >= 10 and hotratio <50:
            return print("...boom")
        else:
            print("...BABOOM!!")



class BoxingGlove(product):
    def __init__(self, weight=10):
        super().__init__(weight)


    def explode(self):
        hotratio = self.weight * self.flammability
        if hotratio < 10:
            return print("...it's a glove.")
        if hotratio >= 10 and hotratio <50:
            return print("...it's a glove.")
        else:
            print("...it's a glove.")



    def punch(self):
        if self.weight < 5:
            return print("that tickles")
        if self.weight >= 5 and <=15:
            return print("hey that hurts")
        else:
            return print("OUCH")
