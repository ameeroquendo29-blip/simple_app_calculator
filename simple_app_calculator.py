#parent class
class CalculatorBase:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
#child class contains operators
class Operator(CalculatorBase):
    def __init__(self, num1, num2, operator):
        super().__init__(num1, num2) #super() = parent class
        self.operator = operator.strip()
    def operations(self):
        if self.operator == '+':
            return self.num1 + self.num2
        elif self.operator == '-':
            return self.num1 - self.num2
        elif self.operator == '*':
            return self.num1 * self.num2
        elif self.operator == '/':
            return self.num1 / self.num2 if self.num2 != 0 else "Error: Division by zero"
        elif self.operator == '^':
            return self.num1 ** self.num2
        elif self.operator == '%':
            return self.num1 % self.num2 if self.num2 != 0 else "Error: Division by zero"
        elif self.operator == '//':
            return self.num1 // self.num2 if self.num2 != 0 else "Error: Division by zero"
        else:
            return "Invalid Operation"
#we will create loop for the calculator
while True:
    print("\nOptions: +, -, *, /, ^, %, // or 'q' to quit")
    operate = input("Choose Operator: ").lower()
    if operate == 'q':
        print("Exiting Calculator. Goodbye!")
        break
    #put the input of val1 and val2 here so if i press q it would not need to ask values before exiting
    val1 = input("Enter the first number: ")
    val2 = input("Enter the second number: ")
    if operate in ('+', '-', '*', '/', '^', '%', '//'):
        try:
            num1 = float(val1)
            num2 = float(val2)
            calc = Operator(num1, num2, operate)
            result = calc.operations()
            print(f"\nRESULT: {result}")
        except ValueError:
            print("Error: Please enter a number")
    else:
        print("Error: Unknown Operation")