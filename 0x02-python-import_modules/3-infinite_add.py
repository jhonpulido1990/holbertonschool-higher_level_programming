#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    value = 0
    f = 0
    if (len(sys.argv)-1) == 0:
        print(0)
    elif (len(sys.argv)-1) == 1:
        print(sys.argv[value + 1])
    elif (len(sys.argv)-1) > 1:
        for w in sys.argv:
            value = value + 1
            if (len(sys.argv)-1) >= value:
                f = f + int(sys.argv[value])
print("{:d}".format(f))
