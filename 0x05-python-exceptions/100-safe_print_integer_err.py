#!/usr/bin/python3
from logging import exception
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value), end='\n')
        return True
    except :
        sys.stderr.write("Exception: Unknown format code 'd' for object of type 'str'\n")
        return False
