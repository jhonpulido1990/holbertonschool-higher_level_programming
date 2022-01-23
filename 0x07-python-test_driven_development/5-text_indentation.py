#!/usr/bin/python3
def text_indentation(text):
    strinspace = ""
    new_space = ""
    if isinstance(text, str):
        text = text.strip()
        text = " ".join(text.split())
        for i in text:
            if '.' in i:
                strinspace += '.    '
            elif '?' in i:
                strinspace += '?    '
            elif ':' in i:
                strinspace += ':    '
            else:
                strinspace += i
        strinspace += ' '
        strinspace = " ".join(strinspace.split())
        for i in strinspace:
            if '.' in i:
                new_space += '.\n\n\n'
            elif '?' in i:
                new_space += '?\n\n\n'
            elif ':' in i:
                new_space += ':\n\n\n'
            else:
                new_space += i
        new_string = new_space.replace('\n ', '')    
        print(new_string, end='')
    else:
        raise TypeError("text must be a string")
