#!/usr/bin/python3
def uppercase(str):
    for w in str:
        character = ord(w)
        if character > 96 and character < 123:
            new_character = chr(character - 32)
        else:
            new_character = w
        print("{}".format(new_character), end="")
    print("")
