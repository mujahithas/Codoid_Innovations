# Find Maximum repeated charcter count in a string


def maximum_char(n):
    list1 = list(n)

    repeated = {}
    for char in list1:
        if char in repeated:
            repeated[char] += 1
        else:
            repeated[char] = 1
    print(repeated)
    print("--------------------------------------------------------------------------------------------")

    maximum_rept_list = []

    for i in repeated:
        if repeated[i] == 2:
            maximum_rept_list.append(i)
    return maximum_rept_list


my_string = "pythonprogrammingtask"

print(maximum_char(my_string))
