#!/usr/bin/python3
import random
nb = random.randint(-10000, 10000)
if nb < 0:
    ld = nb % -10
if nb > 0:
    ld = nb % 10
if ld > 5:
    print("Last digit of {} is {} and is greater than 5".format(nb, ld))
elif ld == 0:
    print("Last digit of {} is {} and is 0".format(nb, ld))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(nb, ld))
