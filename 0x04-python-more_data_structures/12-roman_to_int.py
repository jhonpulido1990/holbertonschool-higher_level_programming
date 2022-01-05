#!/usr/bin/python3
def roman_to_int(roman_string):
    numb = []
    if not roman_string:
        return 0
    for i in roman_string:
        if i == 'I':
            numb.append(1)
        elif i == 'V':
            numb.append(5)
        elif i == 'X':
            numb.append(10)
        elif i == 'L':
            numb.append(50)
        elif i == 'C':
            numb.append(100)
        elif i == 'D':
            numb.append(500)
        elif i == 'M':
            numb.append(1000)
    print(sum(numb))
