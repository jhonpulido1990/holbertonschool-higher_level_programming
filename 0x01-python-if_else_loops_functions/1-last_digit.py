#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_digit = number % 10
    print("{:d} ok {:d}".format(last_digit, number))
if number < 0:
    last_digit = (number * -1) % 10
    print("{:d} ok {:d}".format(last_digit, number))
