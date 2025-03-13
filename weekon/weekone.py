# Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
print("This is a simple calculation code.")

# Ask the user to input two numbers
num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))

# Ask the user to input a valid mathematical operator
op = input("Please enter a valid mathematical operator (+, -, *, /, %): ")

# Perform the operation based on user input
if op == '+':
    result = num1 + num2
    print(f"The sum of the two numbers is: {result}")
elif op == '-':
    result = num1 - num2
    print(f"The difference of the two numbers is: {result}")
elif op == '*':
    result = num1 * num2
    print(f"The product of the two numbers is: {result}")
elif op == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"The quotient of the two numbers is: {result}")
elif op == '%':
    result = num1 % num2
    print(f"The remainder of the two numbers is: {result}")
else:
    print("You entered an invalid operator.")