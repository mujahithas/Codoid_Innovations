# Constructor Overloading


class Vehicle:

    def __init__(self, *arge):
        if len(arge) == 1:
            self.name = arge[0]
        elif len(arge) == 2:
            self.name = arge[0]
            self.colour = arge[1]
        elif len(arge) == 3:
            self.name = arge[0]
            self.colour = arge[1]
            self.model = arge[2]

    def vehicle_detail(self):
        return f"The car name is {self.name} colour is {self.colour} and year of model {self.model}"


maruti = Vehicle("alto", "red", "2021")

print(maruti.vehicle_detail())
print("-------------------------------------------------------------------------------- ")
toyota = Vehicle("innova", "White")
print(toyota.name)
print(toyota.colour)
