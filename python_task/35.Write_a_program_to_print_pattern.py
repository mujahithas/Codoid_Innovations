# Write a program to print pattern?


a = 4
b = 5
for i in range(a,0,-1):
    for j in range(i,0,-1):
        print("*",end="")
    print(" ",end="")
    for j in range(i+1,0,-1):
        print("*",end="")
    print("")




