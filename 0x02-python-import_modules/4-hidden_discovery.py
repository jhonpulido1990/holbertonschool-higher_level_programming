#!/usr/bin/python3
from hidden_4 import *
if __name__ == "__main__":
    name = dir()
    for posit in range(len(name)):
        if not name[posit][0:2] == "__":
            print("{}".format(name[posit]))
