#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (last > 5):
    print('Last digit of {0} is {1[4]} and is greater than 5'.format(number, number))
elif (last == 0):
    print("Last digit of {0} is {1[4]} and is 0".format(number, number))
elif ((last < 5) and (last != 0)):
    print('Last digit of {0} is {1[4]} and is less than 6 and not 0'.format(number, number))
else:
    pass
