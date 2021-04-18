"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is,
3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

sum_square = 0
square_sum = 0

# sum of squares
for i in range(1, 101):
    sum_square += i ** 2

# square of sum
num = range(1, 101)
square_sum = sum(num)
square_sum = square_sum ** 2

diff = square_sum - sum_square

print(sum_square)
print(square_sum)
print(diff)
