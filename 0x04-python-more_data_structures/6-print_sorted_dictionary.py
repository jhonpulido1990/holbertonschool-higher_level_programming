#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    order_dict = sorted(a_dictionary.items())
    for i in range(len(order_dict)):
        print(order_dict[i][0] + ":",order_dict[i][1])
