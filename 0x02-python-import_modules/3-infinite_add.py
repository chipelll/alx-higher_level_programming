#!/usr/bin/python3
import sys


def main():
    if len(sys.argv) < 3:
        print("0")
        return (1)
    a = int(sys.argv[2])
    b = int(sys.argv[1])
    c = a + b
    if len(sys.argv) > 3:
        for i, v in enumerate(sys.argv):
            if i >= 3:
                c += int(sys.argv[i])
    print(c)
    return (0)


if __name__ == "__main__":
    main()
