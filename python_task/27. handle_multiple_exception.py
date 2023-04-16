#Implement a program to handle more than one exception


def calc(a,b,c):
    print(a/b)
    print(c[6])


input1 = int(input("Enter The Number:- "))
input2 = int(input("Enter The Number:- "))
list1 = [10,30,20,10]

try:
    calc(input1,input2,list1)


except ZeroDivisionError:
    print("Zero DivisionError Raised")

except IndexError:
    print("IndexError Raised")

finally:
    print("The program has successfully completed")