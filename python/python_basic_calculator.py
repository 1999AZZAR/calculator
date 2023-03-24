# Define function for addition operation
def add(x, y):
    return x + y

# Define function for subtraction operation
def subtract(x, y):
    return x - y

# Define function for multiplication operation
def multiply(x, y):
    return x * y

# Define function for division operation
def divide(x, y):
    return x / y

# Get the user's choice of operation
print("Please select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    try:
        choice = int(input("Enter your choice (1-4): "))
        if choice not in (1, 2, 3, 4):
            raise ValueError
        break
    except ValueError:
        print("Error: Invalid input. Please enter a valid choice (1-4).")

# Get the user's input for operands
while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        break
    except ValueError:
        print("Error: Invalid input. Please enter a number.")

# Perform the chosen operation and display the result
if choice == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))
else:
    print(num1, "/", num2, "=", divide(num1, num2))

