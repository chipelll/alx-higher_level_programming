#!/usr/bin/python3
for i in range(0, 10):
    for r in range(0, 10):
        if i == r:
            continue
        if i > r:
            continue
        if i != 8:
            print("{:d}{:d}, ".format(i, r), end="")
print(89)
