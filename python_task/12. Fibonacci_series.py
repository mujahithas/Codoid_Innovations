# Write a python Program for Fibonacci series.


def fibonacci(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2,n):
        c = a + b
        a = b
        b = c
        print(c)

n = int(input("Enter the Value :- "))
fibonacci(n)
