#Problem: 02
# Write a program that takes two numbers and an operator (+, -, *, /) and performs the calculation.
# num1,num2=map(int,input("Enter the two number:\n").split())

# Simple calculator program

# Take input from the user
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform calculation based on the operator
if operator == '+':
    result = num1 + num2
    print(f"The result is: {result}")
elif operator == '-':
    result = num1 - num2
    print(f"The result is: {result}")
elif operator == '*':
    result = num1 * num2
    print(f"The result is: {result}")
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"The result is: {result}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operator.")
