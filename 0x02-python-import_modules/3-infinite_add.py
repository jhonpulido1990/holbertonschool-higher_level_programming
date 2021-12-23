#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    value = 0
    f = 0
    for w in sys.argv:
        value = value + 1
        if (len(sys.argv)-1) >= value:
            f = f + int(sys.argv[value])
    print("{:d}".format(f))
