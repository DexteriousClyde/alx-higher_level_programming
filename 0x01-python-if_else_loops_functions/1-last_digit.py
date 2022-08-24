#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of " + str(number) + " is "
int1 = (abs(number) % 10)
if number < 0:
    int1 = -1 * int1
str1 += str(int1) + " "
if int1 > 5:
    str1 += "and is greater than 5"
elif int1 == 0:
    str1 += "and is 0"
else:
    str1 += "and is less than 6 and not 0"
print(str1, end='\n')
