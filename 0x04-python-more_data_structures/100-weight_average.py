#!/usr/bin/python3
def weight_average(my_list=[]):
    num = (sum(x[0] * x[1] for x in my_list)
    num2 = (sum(y[1] for y in my_list) or 1))
    return num/num2 if len(my_list) > 0 else 0
