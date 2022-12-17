#!/usr/bin/python3
import sys


def main():
    i = 0
    if len(sys.argv)  == 2:
                print("1 argument:")
    else:
        if len(sys.argv) == 1:
                print("0 arguments.")
        else: 
                print("{} arguments:".format(((len(sys.argv)) - 1)))

                    
    for i, v in enumerate(sys.argv):
        if i != 0:
            print("{}: {}".format(i, v))


if __name__ == "__main__":
    main()
