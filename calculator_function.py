def sum (num1 , num2):
    return num1 + num2
def subtraction (num1, num2):
    return num1 - num2
def multiplication (num1, num2):
    return num1 * num2
def division (num1, num2):
    if num2 == 0:
        return "Can't be divided by zero."
    else: 
        return num1 / num2
num1 = int(input("enter first number: "))
operation = input("Enter the desired operation e.g., +, -, /, * :")
num2 = int(input("enter second number: "))
if operation == '+':
    print(f"{num1} + {num2} = {sum(num1, num2)}")
if operation == '-':
    print(f"{num1} - {num2} = {subtraction(num1, num2)}")
if operation == '*':
    print(f"{num1} * {num2} = {multiplication(num1, num2)}")
if operation == '/':
    print(f"{num1} / {num2} = {division(num1, num2)}")