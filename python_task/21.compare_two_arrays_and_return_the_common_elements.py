#compare two arrays and return the common elements


def find_common(a, b):
    result = [i for i in a if i in b]
    return result


a = [10, 20, 30, 40, 50]
b = [10,40,50,30,60]


print(find_common(a, b))

