#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)
    a = int(argv[1])
    b = int(argv[3])
    mth = ["+", "-", "*", "/"]
    arr = [add, sub, mul, div]
    for i, j in enumerate(mth):
        if argv[2] == j:
            print("{} {} {} = {}".format(a, j, b, arr[i](a, b)))
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        quit(1)
