#!/usr/bin/python3
def uppercase(str):
    for w in str:
        if ord(w) > 96 and ord(w) < 123:
            character = ord(w) - 32
            w = chr(character)
        print(w, end='')
    print("")
