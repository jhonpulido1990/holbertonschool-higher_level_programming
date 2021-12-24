#!/usr/bin/python3
if __name__ == "__main__":
    value = 0
    from calculator_1 import add, div, sub, mul
    import sys
    for w in sys.argv:
        value = value + 1
    if (value - 1) < 3:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    if operator == '+':
        print('{} + {} = {}'.format(a, b, add(a, b)))
    elif operator == '/':
        print('{} / {} = {}'.format(a, b, div(a, b)))
    elif operator == '-':
        print('{} - {} = {}'.format(a, b, sub(a, b)))
    elif operator == '*':
        print('{} * {} = {}'.format(a, b, mul(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
