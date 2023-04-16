#Implement Exception Handling without Catch block

def calc(a,b):
    ''' The function  is additional,subtract,dividation   '''
    print(a+b)
    print(a/b)
    print(a-b)

input1 = int(input("Enter The Number:- "))
input2 = int(input("Enter The Number:- "))

try:
    calc(input1,input2)

except Exception as e:
    pass

finally:
    print("The program has successfully completed")





