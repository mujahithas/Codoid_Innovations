# swap two numbers without using temporary variable

a = int(input("enter the number for A :- "))
b = int(input("enter the number for B :- "))

a = a+b
b = a-b
a = a- b

print(f"The vale of A after swapping {a}")
print(f"The vale of B after swapping {b}")