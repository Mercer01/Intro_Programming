import math
import random


class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        self.area_circle = self.width * self.height
        return self.area_circle

    def perimeter(self):
        self.perimeter_circle = (self.width * 2) + (self.height * 2)
        return self.perimeter_circle

    def diagonal(self):
        self.diagonal_circle = math.sqrt(
            (self.height ** 2) + (self.width ** 2))
        return self.diagonal_circle

# Testing Rectangle total area
# rect = Rectangle(100, 100)

# print(rect.area())
# print(rect.perimeter())
# print(rect.diagonal())
