# 4. Write a Python script to create a list of first N prime numbers.
N = int(input("Give main value of N: "))
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(n):
    primes = []
    i = 2
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes

print(f"The first {N} prime numbers are: {generate_primes(N)}")
