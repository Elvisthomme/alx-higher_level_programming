#!/usr/bin/python3
"""Square module"""


class Square:
    """Square with size property"""

    def __init__(self, size=0, position=(0, 0)):
        """Create a new square with size"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """The size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """The position of the square"""
        return self.__size

    @position.setter
    def position(self, position):
        if type(position) != tuple\
          or len(position) != 2\
          or type(position[0]) != int\
          or type(position[1]) != int\
          or position[0] < 0\
          or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print  in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    def __str__(self):
        """Print square instance"""
        if self.__size == 0:
            return ""
        else:
            string = ""
            for i in range(self.__position[1]):
                string += '\n'
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    string +=' '
                for j in range(self.__size):
                    string += '#'
                string += '\n'
        return string[:-1]
