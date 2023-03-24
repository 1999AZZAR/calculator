from typing import List

def fibonacci(fMax: int) -> List[int]:
    F, Fp, Fn = 1, 0, 0
    fib = []
    while Fp <= fMax:
        fib.append(Fp)
        Fn = F + Fp
        Fp = F
        F = Fn
    return fib

# --- END FIBONACCI FUNCTION ---

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

