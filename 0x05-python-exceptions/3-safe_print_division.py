#!/usr/bin/python3
from unittest import result


def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
        return result
    except:
        return None
    finally:
        print("Inside result: {}".format(result))
