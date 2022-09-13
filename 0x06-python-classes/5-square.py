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

    def area(self):
        """Area of the square.
        Returns:
            size squared.
        """
        return self.__size ** 2

    @property
    def size(self):
        """ Accessor method to get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """ setter method to set the size of the square"""
        if type(value) == int:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        """prints the square with hash # symbols in between"""
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
        else:
            print()
