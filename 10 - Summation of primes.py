"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

*My original code looped through every single number from 2 to 2000000 to check if it was prime then added it to the
total. However, that obviously took a lot of time. I learnt about the Sieve of Eratosthenes which is an ancient Greek
algorithm for finding all prime numbers up to any given limit. I was proud of how quickly the code ran after
implementing this, hence the runtime count.
"""

import time
start = time.time()


def sum_primes(n):
    total = 0
    sieve = [True] * n
    for p in range(2, n):
        if sieve[p]:
            total += p
            for i in range(p*p, n, p):
                sieve[i] = False
    return total


print(sum_primes(2000000))
elapsed = (time.time() - start)
print(f"Runtime: {elapsed} seconds")
