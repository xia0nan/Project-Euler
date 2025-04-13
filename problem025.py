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
def find_fibonacci_index(num_digits):
    """
    Find the index of the first Fibonacci number with the specified number of digits.
    
    Args:
        num_digits: The number of digits to look for
        
    Returns:
        The index of the first Fibonacci number with num_digits digits
    """
    # Initialize the first two Fibonacci numbers
    a, b = 1, 1
    index = 2  # We start with F₂
    
    # Continue generating Fibonacci numbers until we find one with the desired number of digits
    while len(str(b)) < num_digits:
        a, b = b, a + b
        index += 1
    
    return index

result = find_fibonacci_index(1000)
print(f"The index of the first term in the Fibonacci sequence to contain 1000 digits is {result}")
