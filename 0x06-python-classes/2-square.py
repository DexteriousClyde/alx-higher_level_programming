#!/usr/bin/python3
"""Square class."""


class Square:
    """square attributes"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
