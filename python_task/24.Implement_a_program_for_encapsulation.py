
#Implement a program for encapsulation

class Vehicle:

    def __init__(self, name, colour, model):
        self.name = name
        self.colour = colour
        self.model = model

    def car(self):
        print("The car company name is ", self.name)
        print("The car colour is ", self.colour)
        print("The car model is ", self.model)


cruiser = Vehicle("Toyota","white",2022)

cruiser.car()