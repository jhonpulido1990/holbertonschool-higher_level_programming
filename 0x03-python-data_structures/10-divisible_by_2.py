#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list =[]
    for i in my_list:
        if i % 2 == 0:
            condition = True
        else:
            condition = False
        new_list.append(condition)
    return new_list
