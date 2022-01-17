#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lent = 0
    resuk = []
    while(lent < list_length):
        try:
            resuk.append(my_list_1[lent] / my_list_2[lent])
        except(IndexError):
            print("out of range")
            resuk.append(0)
        except (TypeError):
            print("wrong type")
            resuk.append(0)
        except(ZeroDivisionError):
            print("division by 0")
            resuk.append(0)
        lent += 1
    return resuk
