class CalculatorBase:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

print("Select Operation")
print("1. + ")
print("2. - ")
print("3. * ")
print("4. / ")
print("5. % ")
print("6. ** ")
print("7. reciprocal")
print("8. root")
choice = int(input("Enter your choice: "))
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
