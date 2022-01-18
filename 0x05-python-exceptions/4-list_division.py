#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lent = 0
    tmp = 0
    resuk = []
    while(lent < list_length):
        try:
            tmp = my_list_1[lent] / my_list_2[lent]
        except(IndexError):
            print("out of range")
            tmp = 0
        except (TypeError):
            print("wrong type")
            tmp = 0
        except(ZeroDivisionError):
            print("division by 0")
            tmp = 0
        finally:
            pass
        lent += 1
        resuk.append(tmp)
    return resuk
