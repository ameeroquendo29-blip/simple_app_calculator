#parent class
class CalculatorBase:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
#child class contains operators
class Operator(CalculatorBase):
    def __init__(self, num1, num2, operator):
        super().__init__(num1, num2) #super() = parent class
        self.operator = operator
    def operations(self):
        if self.operation == '+':
            return self.num1 + self.num2
        elif self.operation == '-':
            return self.num1 - self.num2
        elif self.operation == '*':
            return self.num1 * self.num2
        elif self.operation == '/':
            return self.num1 / self.num2 if self.num2 != 0 else "Error: Division by zero"
        elif self.operation == '^':
            return self.num1 ** self.num2
        elif self.operation == '%':
            return self.num1 % self.num2 if self.num2 != 0 else "Error: Division by zero"
        elif self.operation == '//':
            return self.num1 // self.num2 if self.num2 != 0 else "Error: Division by zero"
        else:
            return "Invalid Operation"
#we will create loop for the calculator
while True:
    print("\nOptions: +, -, *, /, ^, %, // or 'q' to quit")
    operate = input("Choose Operator: ").lower()