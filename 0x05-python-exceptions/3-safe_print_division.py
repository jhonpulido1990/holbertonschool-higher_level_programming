#!/usr/bin/python3
def safe_print_division(a, b):
    resul = None
    try:
        resul = a / b
        return resul
    except:
        return None
    finally:
        print("Inside result: {}".format(resul))
