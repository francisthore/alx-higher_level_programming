#!/usr/bin/python3

"""This is a module that defines a rectangle"""


class Rectangle:
    """This class defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Init method to set the initial values for the
        height and width
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print the string representation of the rectangle"""
        res = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for n in range(self.__width):
                res += str(self.print_symbol)
            if i < self.__height - 1:
                res += "\n"
        return res

    def __repr__(self):
        """Returns the string represantantion of an object"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Instance deletion behavior"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
