"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""


def is_prime(n):
    if n < 2:
        pass
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# returns the nth prime number
def nth_prime(n):
    number_of_primes = 0
    prime = 1

    while number_of_primes < n:
        prime += 1
        if is_prime(prime):
            number_of_primes += 1
    return prime


print(nth_prime(10001))
