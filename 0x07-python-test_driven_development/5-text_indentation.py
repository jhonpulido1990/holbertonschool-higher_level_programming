#!/usr/bin/python3
def text_indentation(text):
    strinspace = ""
    if isinstance(text, str):
        text = text.strip()
        text = " ".join(text.split())
        for i in text:
            if '.' in i:
                strinspace +=  '.\n\n\n'
            elif '?' in i:
                strinspace += '?\n\n\n'
            elif ':' in i:
                strinspace += ':\n\n\n'
            else:
                strinspace += i
        new_string = strinspace.replace('\n ', '')
        
        print(new_string)
    else:
        raise TypeError("text must be a string")