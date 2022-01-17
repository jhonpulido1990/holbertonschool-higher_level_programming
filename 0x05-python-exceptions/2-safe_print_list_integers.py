#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    a = 0
    b = 0
    while (x > a):
        try:
            if type(my_list[a]) == int:
                print("{}".format(my_list[a]), end='')
                b = b + 1
        except (ValueError, TypeError):
            pass
        a = a + 1
    print()
    return b
