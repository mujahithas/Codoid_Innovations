#Write a program in python to check whether number is palindrom or not using recursive method

number = int(input("Enter The Value:- "))

def reverse_num(n):
    if n<10:
        return 1
    else:
        return int(str(n%10)+str(reverse_num(n//10)))

def palindrom(number):

    if number == reverse_num(number):
        return 1
    return 0

if palindrom(number) ==1:
    print(f"{number} is a palindrom ")
else:
    print(f"{number} is a not palindrom ")


