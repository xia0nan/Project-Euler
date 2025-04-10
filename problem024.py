"""
Author: Nan <xnone0104@gmail.com>

https://projecteuler.net/problem=24

[Lexicographic Permutations]
Problem 24

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""
import math

# Initialize variables
digits = list(range(10))         # Digits 0 through 9
k = 999_999                      # 1,000,000th permutation (0-based index)
result = []                      # To store the resulting permutation

# Construct the permutation
for i in reversed(range(1, len(digits))):
    fact = math.factorial(i)     # Number of permutations for each block
    index = k // fact            # Select the correct digit index
    result.append(digits.pop(index))  # Add the digit to result
    k %= fact                    # Update k to the new position within the block

# Add the final remaining digit
result += digits

# Convert the result to an integer
millionth_permutation = int(''.join(map(str, result)))
print(millionth_permutation)
