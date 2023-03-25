def is_prime(n): 
    if n <= 1: 
        return False 
    for i in range(2, int(n**0.5)+1): 
        if n % i == 0: 
            return False 
    return True 

def fibonacci_sequence(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def prime_and_fibonacci(n): 
    if not isinstance(n, int) or n > 10000: 
        return "Invalid input. Please enter an integer less than or equal to 10000." 

    prime_numbers = [i for i in range(2, n**2) if is_prime(i)][:n]
    fibonacci_numbers = fibonacci_sequence(n)

    return prime_numbers, fibonacci_numbers

while True:
    print("Please choose an option:")
    print("1. Generate a list of prime numbers")
    print("2. Generate a list of Fibonacci numbers")
    print("3. Generate both lists")

    choice = input("Enter 1, 2, or 3: ")

    if choice not in ["1", "2", "3"]:
        print("Invalid choice. Please enter 1, 2, or 3.")
        continue

    n = input("Enter a positive integer: ")
    try:
        n = int(n)
        if n < 1:
            raise ValueError("Input must be positive.")
        elif n > 10000:
            raise ValueError("Input must be less than or equal to 10000.")
    except ValueError as err:
        print(f"Invalid input: {err}")
    else:
        if choice == "1":
            prime_numbers = [i for i in range(2, n**2) if is_prime(i)][:n]
            print(f"The first {n} prime numbers are:", prime_numbers)
        elif choice == "2":
            fibonacci_numbers = fibonacci_sequence(n)
            print(f"The first {n} Fibonacci numbers are:", fibonacci_numbers)
        else:
            prime_numbers, fibonacci_numbers = prime_and_fibonacci(n)
            print(f"The first {n} prime numbers are:", prime_numbers)
            print(f"The first {n} Fibonacci numbers are:", fibonacci_numbers)

        response = input("Do you want to generate another set of numbers? (y/n) ")
        if response.lower() != "y":
            break

