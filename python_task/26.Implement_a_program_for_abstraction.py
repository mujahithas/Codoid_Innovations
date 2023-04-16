#Implement a program for abstraction

#puplic
#private
#protector

class Parent:

    def play_ground(self):#puplic can access this method
        print("This is home play_ground")

    def _house_key(self):#private can access only subclass this method
        print("This is house key")

    def __creditcard(self):#protector can access only Parent this method

        print("This is parend creditcard")


class Son(Parent):
    pass

son1 = Son()

son1.play_ground()
son1._house_key()
