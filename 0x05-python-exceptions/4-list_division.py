#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    arr = []
    while i < list_length:
        arr_element
        try:
            arr_element = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            arr_element = 0
        except ZeroDivisionError:
            print("division by 0")
            arr_element = 0
        except IndexError:
            print("out of range")
            arr_element = 0
        finally:
            arr.append(arr_element)
            i += 1
    return arr
