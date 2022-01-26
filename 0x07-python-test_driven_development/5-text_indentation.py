#!/usr/bin/python3
'''create funtion that identation
each line of text

example:
use text_ identation(text to identation)'''


def text_indentation(text):
    '''funtion that concat string and
    add line break and delecte space repeat
    create a new string and save on it'''
    strinspace = ""
    new_space = ""
    if isinstance(text, str):
        for i in ".?:":
            text = text.replace(i, i + '\n\n')
        strinspace = [charact.strip(' ') for charact in text.split("\n")]
        new_space = "\n".join(strinspace)
        print(new_space, end='')
    else:
        raise TypeError("text must be a string")
