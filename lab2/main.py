import math
from arctan import Arctan
from arccot import Arccot


def main():

    arctan_func = Arctan(1)
    print("Значение арктангенса:", arctan_func.calculate())

    arctan_derivative = arctan_func.derivative()
    print("Значение производной арктангенса:", arctan_derivative.calculate())

    arctan_second_derivative = arctan_func.second_derivative()
    print("Значение второй производной арктангенса:", arctan_second_derivative.calculate())

    arccotan_func = Arccot(2)
    print("Значение арккотангенса:", arccotan_func.calculate())

    arccotan_derivative = arccotan_func.derivative()
    print("Значение производной арккотангенса:", arccotan_derivative.calculate())

if __name__ == "__main__":
    main()
