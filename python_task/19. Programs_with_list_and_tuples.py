# Programs with list and tuples

# A tuple is an immutable data structure in Python, which means that it cannot be changed or modified once it is
# created. This includes adding, deleting, or modifying elements in the tuple. Any attempt to modify a tuple will
# result in a TypeError.

my_tuple = ("python","selenium",2022)

print(type(my_tuple))
print("-------------------------------------------------------------")

# a list is a mutable python data structure, which means that it can be changed or modified after it is created

my_list =["python","selenium",2022]
print(f"{my_list}The before modification ")
print("--------------------------------------------------------------- ")
my_list[0]="java"
print(f"{my_list}The after modification ")

