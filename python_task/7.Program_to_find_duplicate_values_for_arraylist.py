# Program to find duplicate values for ArrayList


mylist = [10, 10, 10, 20, 20, 30, 40, 50]
dup_list = []


def find_duplicate_num(n):
    for i in n:
        if n.count(i)>1:
         if i not in dup_list:
                dup_list.append(i)
    return dup_list


print(find_duplicate_num(mylist))
