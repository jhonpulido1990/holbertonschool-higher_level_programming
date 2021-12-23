#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    value = 0
    if (len(sys.argv)-1) == 0:
        print("{} arguments.".format((len(sys.argv)-1)))
    elif (len(sys.argv)-1) == 1:
        print("{} argument:".format((len(sys.argv)-1)))
    else:
        print("{} arguments:".format((len(sys.argv)-1)))
    for w in sys.argv:
        value = value + 1
        if (len(sys.argv)-1) >= value:
            print("{}:".format(value), sys.argv[value])
