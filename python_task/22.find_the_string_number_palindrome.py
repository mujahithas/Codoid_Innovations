#Write a python Program to find whether a string or number is palindrome or not. tamil


def find_palindrome(n):
    rever_n = n[::-1]

    if rever_n == n:
        print("It is palindrome")
    else:
        print("It is not palindrome")

value = input("Enter the Value :- ")

find_palindrome(value)
