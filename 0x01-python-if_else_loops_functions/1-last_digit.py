#!/usr/bin/python3
import random
nb = random.randint(-10000, 10000)
if nb < 0:
    ld = nb % -10
if nb > 0:
    ld = nb % 10
if ld > 5:
    print("Last digit of", nb, "is", ld, "and is greater than 5")
elif ld == 0:
    print("Last digit of", nb, "is", ld, "and is 0")
else:
    print("Last digit of", nb, "is", ld, "and is less than 6 and not 0")
