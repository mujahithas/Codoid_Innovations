# Write a program to check the vowels in the string.

def find_vowels(n):
    vowels = "aeiou"

    for letter in n:
        for v in vowels:
            if letter==v:
                print(v,end=" ")
my_strg = "Codoid Innovations"

find_vowels(my_strg)