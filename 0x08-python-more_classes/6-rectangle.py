#!/usr/bin/python3

"""Defines a Rectangle"""

class Rectangle:
    """
    Creates a Recangle
    
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """"
        initialize the class rectangle
        Keyword Arguments:
            width {int} -- width of the rectangle (default: {0})
            height {int} -- height of the rectangle (default: {0})
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    
    @property
    def width(self):
        """gets the width
        returns width of rectangle
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """sets function to with
        Arguments:
             value {int} -[value of width]
        Raises:
             TypeError: width must be an integer
             ValueError: width must be >= 0
        """
        if type(value) != int:
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        
        self.__width = value

    @property
    def height(self):
        """gets the height
        returns height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """sets function to height
        Arguments:
             value {int} -[value of height]
        Raises:
             TypeError: height must be an integer
             ValueError: height must be >= 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        
        self.__height = value
    
    def area(self):
        """
        Calculates area of Rectangle
        Returns: area of rectangle 

        """
        self.area = self.__width * self.__height
        return self.area
    
    def perimeter(self):
        """
        Calculates perimeter of Rectangle
        Returns: perimeter of rectangle 

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        self.perimeter = self.__width + self.__height + self.__width + self.__height

        return self.perimeter
    
    def __str__(self):
        """ 
        Method that gets the string representation of the rectangle
        Returns:
            string -- string representation
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return 0
        for row in range(self.__height):
            for col in range(self.__width):
                string = string + '#'
            string = string + '\n'
        return string[:-1]
    
    def __repr__(self):
        """
        Return string of the rectangle

        """
        return f"Rectangle({self.__width}, {self.__height})"
    
    def __del__(self):
        """Print a message for every deletion of
        the rectangle.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
        
