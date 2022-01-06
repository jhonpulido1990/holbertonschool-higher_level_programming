#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == None:
        return 0
    a = []
    b = []
    for i in range(len(my_list)):
        a.append(my_list[i][0] * my_list[i][1])
        b.append(my_list[i][1])
    result = sum(a)/sum(b)
    return result
