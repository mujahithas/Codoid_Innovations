# remove duplicates from sorted array

def remove_duplicate(n):
    list1 = []
    for i in n:
        if i not in list1:
            list1.append(i)
    return list1

my_list = [10, 10, 20, 30, 40, 50, 60, 70, 70, 80, 80, 90, 100, 100]

print(remove_duplicate(my_list))
