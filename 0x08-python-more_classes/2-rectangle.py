#!/usr/bin/python3
"""Area and Perimeter"""


class Rectangle:
    """Defines the implementation of a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """Property retriever, for retreiving"""
        return self.__width
    
    @width.setter
    def width(self, value):
        
        if type(value) != int:
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        
        self.__width = value

    @property
    def height(self):
        """Property retriever, for retreiving
        the rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        
        self.__height = value
    
    def area(self):
        """Public instance method that returns
        the rectangle area
        """
        self_area = self.__width * self.__height
        return self_area
    
    def perimeter(self):
        """Public instance method that returns the
        rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        self_perimeter = self.__width + self.__height + self.__width + self.__height

        return self_perimeter