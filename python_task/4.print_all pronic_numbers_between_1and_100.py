
# Print all pronic numbers between 1 and 100

def pronic_number(n):
    flag = 0

    for i in range(1, n + 1):
        if (i * (i + 1)) == n:
            flag = 1
            break;
    return flag


print("Pronic numbers between 1 and 100: ")
for p in range(1, 101):
    if pronic_number(p):
        print(p,end=" ")