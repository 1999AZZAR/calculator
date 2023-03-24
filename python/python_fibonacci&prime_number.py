def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def fibonacci_sequence(n):
    fib = [0, 1]
    while fib[-1] <= n:
        fib.append(fib[-1] + fib[-2])
    return fib[:-1]

def prime_and_fibonacci(n):
    if not isinstance(n, int) or n > 10000:
        return "Invalid input. Please enter an integer less than or equal to 10000."

    prime_numbers = [i for i in range(2, n+1) if is_prime(i)]
    fibonacci_numbers = fibonacci_sequence(n)

    return (prime_numbers, fibonacci_numbers)

while True:
    n = input("Enter a number: ")
    try:
        n = int(n)
        if n < 1:
            raise ValueError("Input must be not zero or non-negative.")
        elif n > 1000000:
            raise ValueError("Input must be less than or equal to 1000000.")
    except ValueError as err:
        print(f"Invalid input: {err}")
    else:
        prime_numbers, fibonacci_numbers = prime_and_fibonacci(n)
        print("Prime numbers:", prime_numbers)
        print("Fibonacci numbers:", fibonacci_numbers)
        break

