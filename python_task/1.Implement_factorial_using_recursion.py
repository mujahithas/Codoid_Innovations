
# 1.Implement factorial using recursion

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("Enter The Value: "))

result = factorial(n)
print("factorial: ", result)



