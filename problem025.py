"""
Author: Nan <xnone0104@gmail.com>

https://projecteuler.net/problem=25

[1000-digit Fibonacci Number]
Problem 25

The Fibonacci sequence is defined by the recurrence relation:

    Fₙ = Fₙ₋₁ + Fₙ₋₂, where F₁ = 1 and F₂ = 1.

Hence the first 12 terms will be:

    F₁  = 1
    F₂  = 1
    F₃  = 2
    F₄  = 3
    F₅  = 5
    F₆  = 8
    F₇  = 13
    F₈  = 21
    F₉  = 34
    F₁₀ = 55
    F₁₁ = 89
    F₁₂ = 144

The 12th term, F₁₂, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

"""

from decimal import Decimal, getcontext

def fibonacci_index_with_digits_precise(digits):
    # Set precision high enough to handle large digit calculations
    getcontext().prec = 100  # 100 digits of precision is enough for 10000-digit Fibonacci

    sqrt_5 = Decimal(5).sqrt()
    phi = (Decimal(1) + sqrt_5) / 2

    log_phi = phi.ln() / Decimal(10).ln()  # log10(phi)
    log_sqrt_5 = (sqrt_5.ln() / Decimal(10).ln())  # log10(sqrt(5))

    index = (Decimal(digits) - 1 + log_sqrt_5) / log_phi
    return int(index.to_integral_value(rounding='ROUND_CEILING'))

# Example: 1000-digit Fibonacci number
print("The index of the first term in the Fibonacci sequence to contain 1000 digits is", 
      fibonacci_index_with_digits_precise(1000))

# Example: 10000-digit Fibonacci number
print("The index of the first term in the Fibonacci sequence to contain 10000 digits is",
      fibonacci_index_with_digits_precise(10000))
