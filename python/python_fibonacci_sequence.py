def fibonacci_sequence(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

while True:
    n = input("Enter the number of Fibonacci numbers to generate: ")
    try:
        n = int(n)
        if n < 1:
            raise ValueError("Input must be positive.")
        elif n > 1000000:
            raise ValueError("Input must be less than or equal to 1000000.")
    except ValueError as err:
        print(f"Invalid input: {err}")
    else:
        fibonacci_numbers = fibonacci_sequence(n)
        print(f"The first {n} Fibonacci numbers are:", fibonacci_numbers)
        response = input("Do you want to generate another set of Fibonacci numbers? (y/n) ")
        if response.lower() != "y":
            break

