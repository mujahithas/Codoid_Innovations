# write a program to print all the prime numbers between two numbers
#Between 1 and 10 between 20 to 30

def find_prime_num(a, b):
    for num in range(a, b + 1):
        count = 0
        for i in range(1, num + 1):
            if (num % i) == 0:
                count = count + 1

        if count == 2:
            print(num,end =" ")


find_prime_num(1,10)

print(" ")

find_prime_num(20,30)

