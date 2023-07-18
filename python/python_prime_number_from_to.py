def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

if __name__ == "__main__":
    start_range = 0
    end_range = 100

    prime_numbers = find_primes(start_range, end_range)
    print("Bilangan prima dari", start_range, "hingga", end_range, "adalah:")
    print(prime_numbers)
