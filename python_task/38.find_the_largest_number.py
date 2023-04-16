
# Find the largest number in the array (without using pre define functions)


def find_max_num(n):
    max_num = n[0]

    for i in n:
        if i > max_num:
            max_num=i
    return max_num
my_list = [10,20,30,40,50,1000]

print(find_max_num(my_list))

