import math

from derivative import Derivative
from function import Function


class Arccot(Function):

    def calculate(self):
        return math.atan(1 / self.x)

    def derivative(self):
        return Derivative(-1 / (1 + self.x ** 2))
