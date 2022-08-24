#!/usr/bin/python3
def remove_char_at(str1, n):
    if n < 0:
        return str1
    return (str1[0:n] + str1[n + 1:])
