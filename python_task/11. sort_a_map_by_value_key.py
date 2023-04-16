# Implement a program to sort a map by value / Key

def sort_dect(n):
    sort_list = sorted(n.keys())
    list1 = []
    for i in sort_list:
        list1.append(n[i])
    d1 = dict(zip(sort_list, list1))
    return (f"Sorted Dictionary {d1}")


student_mark = {"st1": 85, "st4": 75, "st3": 68, "st2": 50}

print(sort_dect(student_mark))
