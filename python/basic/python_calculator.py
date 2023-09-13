from math import sqrt
from typing import List

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def fibonacci(fMax: int) -> List[int]:
    F, Fp, Fn = 1, 0, 0
    fib = []
    while Fp <= fMax:
        fib.append(Fp)
        Fn = F + Fp
        Fp = F
        F = Fn
    return fib

def validate_input(num):
    if num is None or num == "":
        return False, "Type anything!"
    elif int(num) <= 2:
        return False, "Oh no! You need to pick a higher number to make me work!"
    elif int(num) > 10000:
        return False, "Please, pick something smaller."
    elif not num.isnumeric():
        return False, "Snap! It looks like you didn't type a number."
    else:
        return True, ""

def generate_primes(num):
    primes = []
    for i in range(2, num+1):
        if all(i % j != 0 for j in range(2, int(sqrt(i))+1)):
            primes.append(i)
    return primes

# Get the user's choice of operation
print("Please select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Generate Fibonacci sequence")
print("6. Generate prime numbers")

while True:
    try:
        choice = int(input("Enter your choice (1-6): "))
        if choice not in (1, 2, 3, 4, 5, 6):
            raise ValueError
        break
    except ValueError:
        print("Error: Invalid input. Please enter a valid choice (1-6).")

# Perform the chosen operation and display the result
if choice in (1, 2, 3, 4):
    # Get the user's input for operands
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
    
    if choice == 1:
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == 2:
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == 3:
        print(num1, "*", num2, "=", multiply(num1, num2))
    else:
        print(num1, "/", num2, "=", divide(num1, num2))

elif choice == 5:
    # Get the maximum value from user input
    while True:
        try:
            fMax = int(input("Enter a number to change the max value for the Fibonacci sequence: "))
            if fMax < 1:
                print("Error: The number must be greater than zero.")
            else:
                break
        except ValueError:
            print("Error: Invalid input. Please enter a positive integer.")

    # Generate the Fibonacci sequence up to fMax
    fib = fibonacci(fMax)

    # Display the Fibonacci sequence on the page
    print(", ".join(map(str, fib)))

else:
   # Get the user's input for generating prime numbers
   while True:
       user_input = input("Type any number to display prime numbers: ")
       is_valid, error_msg = validate_input(user_input)
       if is_valid:
           primes = generate_primes(int(user_input))
           final_numbers = ', '.join(str(p) for p in primes)
           print("Prime numbers smaller than your number: " + final_numbers)
           break
       else:
           print(error_msg)
