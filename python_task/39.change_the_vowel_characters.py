# Change the vowel characters to ”S”
#          Python          Pythsn

def change_str(n,s):
    vowels = "aeiou"

    for i in vowels:
        n= n.replace(i,s)
    return n

my_str = "python"
s = "s"

print(change_str(my_str,s))


