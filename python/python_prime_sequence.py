def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def generate_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

while True:
    n = input("Enter the number of prime numbers to generate: ")
    try:
        n = int(n)
        if n < 1:
            raise ValueError("Input must be positive.")
        elif n > 1000000:
            raise ValueError("Input must be less than or equal to 1000000.")
    except ValueError as err:
        print(f"Invalid input: {err}")
    else:
        primes = generate_n_primes(n)
        print(f"The first {n} prime numbers are:", primes)
        response = input("Do you want to generate another set of prime numbers? (y/n) ")
        if response.lower() != "y":
            break

