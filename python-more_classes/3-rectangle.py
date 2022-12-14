#!/usr/bin/python3
"""This module defines the class Rectangle"""


class Rectangle:
    """Definition of class Rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """calculates the area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return (0)
        return (2 * self.width + 2 * self.height)

    def __str__(self):
        """Return a nice rectangle made with the char '#'"""
        if self.__height != 0 and self.__width != 0:
            rec_print = ""
            for i in range(self.__height):
                for j in range(self.__width):
                    rec_print += '#'
                rec_print += '\n'
            return rec_print[:-1]
        else:
            return ""
