# Python program to determine whether the given number is a Harshad Number

n = input("enter The value ")

my_list = list(map(int, n))
list_sum = sum(my_list)

if int(n) % list_sum == 0:
    print((f"{n} It is harshad Number"))
else:
    print((f"{n} It is not a harshad Number"))
