#!/usr/bin/python3
from copy import copy
from pickle import APPEND


def list_division(my_list_1, my_list_2, list_length):
    lent = 0
    resuk = []
    while(lent < list_length):
        try:
            if(my_list_1[lent] != 0 or my_list_2[lent] != 0):
                try:
                    if(int(my_list_1[lent]) and int(my_list_2[lent])):
                        try:
                            if (my_list_1[lent] and my_list_2[lent]):
                                resuk.append(my_list_1[lent] / my_list_2[lent])
                        except:
                            print("out of range")
                            resuk.append(0)
                except:
                    print("wrong type")
                    resuk.append(0)
        except:
            print("division by 0")
            resuk.append(0)
        lent += 1
    return resuk
