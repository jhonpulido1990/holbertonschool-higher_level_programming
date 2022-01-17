#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    for j in my_list:
        try:
            if j <= x:
                print("{}".format(my_list[j - 1]), end='')
                a = a + 1
        except:
            break;
    print()
    return a
