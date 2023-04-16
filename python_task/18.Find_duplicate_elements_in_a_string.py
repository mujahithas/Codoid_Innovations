#Find duplicate elements in a string

def find_duplicate(n):

    dub_str_list = []

    for i in n:
        if n.count(i)>1:
            if i not in dub_str_list:
                dub_str_list.append(i)
    return dub_str_list

my_string = "python program"

print(find_duplicate(my_string))


