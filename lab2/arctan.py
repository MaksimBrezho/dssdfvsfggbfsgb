import math

from derivative import Derivative
from function import Function


class Arctan(Function):

    def calculate(self, name):
        print(name)
        return math.atan(self.x)

    #def derivative(self):
    #   return Derivative(1 / (1 + self.x ** 2))

    def derivative(self):
        return Derivative(1 / (1 + self.x ** 2))

    def second_derivative(self):
        return Derivative(-(2 * self.x) / ((1 + self.x ** 2) ** 2))