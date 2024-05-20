from function import Function


class Derivative(Function):

    def __init__(self, derivative_value):
        self.derivative_value = derivative_value

    def calculate(self):
        return self.derivative_value

    def second_derivative(self):
        raise NotImplementedError("Метод second_derivative должен быть переопределен в наследниках.")
