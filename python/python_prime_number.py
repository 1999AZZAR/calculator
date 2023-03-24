from math import sqrt

def validate_input(num):
    if num is None or num == "":
        return False, "Type anything!"
    elif int(num) <= 2:
        return False, "Oh no! You need to pick a higher number to make me work!"
    elif int(num) > 1000:
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

user_input = input("Type any number to display prime numbers: ")
is_valid, error_msg = validate_input(user_input)

if is_valid:
    primes = generate_primes(int(user_input))
    final_numbers = ', '.join(str(p) for p in primes)
    print("Prime numbers smaller than your number: " + final_numbers)
else:
    print(error_msg)

