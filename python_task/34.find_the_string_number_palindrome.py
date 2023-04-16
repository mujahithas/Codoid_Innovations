#Write a python Program to find whether a string or number is palindrome or not. tamil


def find_palindrome(n):
    rever_n = n[::-1]

    if rever_n == n:
        print(f"{n} It is palindrome")
    else:
        print(f"{n} It is not palindrome")

find_palindrome("madam")
print("-----------------------------------------------------------------")
find_palindrome("wow")
print("-----------------------------------------------------------------")
find_palindrome("cycle")
print("-----------------------------------------------------------------")