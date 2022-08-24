#!/usr/bin/python3
import random
number = random.randint(-10, 10)
str1 = str(number) + " "
if number > 0:
	str1 += "is positive"
elif number < 0:
	str1 += "is negative"
else:
	str1 += "is zero"
print(str1, end = '\n')
