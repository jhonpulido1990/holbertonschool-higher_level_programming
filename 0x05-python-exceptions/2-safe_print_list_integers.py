#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    a = 0
    b = 0
    while (x > a):
        try:
            if (a) < x:
                if type(my_list[a]) == int:
                    print("{}".format(my_list[a]), end='')
                    b = b + 1
                a = a + 1
        except (ValueError, TypeError):
            pass
    print()
    return b
