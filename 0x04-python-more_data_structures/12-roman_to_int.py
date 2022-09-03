#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string == None:
        return 0;
    ret = 0
    num = = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in reversed(roamn_string):
        ret += num[i] if total < num[i] * 5 else -num[i]
    return ret
