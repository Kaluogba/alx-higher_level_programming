#!/usr/bin/python3

def element_at(my_list, idx):
    for i in range(my_list):
        if idx < 0:
            return None
        elif idx > (len(my_list) + 1):
            return None
        else:
            return("{:d}".format(my_list.index(idx)))


print(element_at([1, 2, 3], 3))
