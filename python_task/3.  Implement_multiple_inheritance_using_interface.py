# 3.Implement multiple inheritance using interface

class Vehicle:

    def __init__(self, name, colour, model):
        self.name = name
        self.colour = colour
        self.model = model

    def car(self):
        print("The car company name is ", self.name)
        print("The car colour is ", self.colour)
        print("The car model is ", self.model)


class EngineType:
    def __init__(self,engine_type):
        self.engine_type = engine_type

    def drive_type(self):
        print(self.engine_type,"drive type")


class Toyota(Vehicle,EngineType):
    def __init__(self, name, colour, model,engine_type):

        Vehicle.__init__(self, name, colour, model)
        EngineType.__init__(self,engine_type)


car1 = Toyota("innova crysta","blue","2021","four wheel")

car1.car()
car1.drive_type()