# Implement method overloading

def func_sum(a=None, b=None, c=None):
    if a!= None and b != None and c != None:
        return a + b + c
    else:
        return a + b


sum_two_num = func_sum(10,20)
sum_three_num = func_sum(10,20,30)

print(sum_two_num)
print(sum_three_num)

# Implement method over riding

class Parent:

    def bike(self):
        print("This is father's bike")

    def mobile(self):
        print("This is father's mobile")

class Child(Parent):
    def mobile(self):
        print("This is son's mobile")


child1 = Child()
child1.bike()
child1.mobile()