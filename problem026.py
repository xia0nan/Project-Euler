"""
Author: Nan <xnone0104@gmail.com>

https://projecteuler.net/problem=26

[Reciprocal Cycles]
Problem 26

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2  = 0.5
1/3  = 0.(3)
1/4  = 0.25
1/5  = 0.2
1/6  = 0.1(6)
1/7  = 0.(142857)
1/8  = 0.125
1/9  = 0.(1)
1/10 = 0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

def get_cycle_length(denominator):
    """
    Calculates the length of the recurring cycle for the unit fraction 1/denominator.
    Uses long division simulation.
    """
    if denominator <= 1:
        return 0
    
    remainders = {} # Stores remainder -> position mapping
    numerator = 1
    position = 0
    
    while numerator != 0:
        # If we've seen this numerator (remainder) before, a cycle is found
        if numerator in remainders:
            first_occurrence_position = remainders[numerator]
            return position - first_occurrence_position
        
        # Store the current numerator and its position
        remainders[numerator] = position
        
        # Perform one step of long division: multiply numerator by 10 and take remainder
        numerator = (numerator * 10) % denominator
        position += 1
        
    # If numerator becomes 0, the decimal terminates (no recurring cycle)
    return 0

def solve_problem26():
    """
    Finds the value of d < 1000 for which 1/d has the longest recurring cycle.
    """
    max_length = 0
    result_d = 0
    
    for d in range(2, 1000):
        current_length = get_cycle_length(d)
        if current_length > max_length:
            max_length = current_length
            result_d = d
            
    return result_d, max_length

if __name__ == "__main__":
    d, length = solve_problem26()
    print(f"The value of d < 1000 for which 1/d contains the longest recurring cycle is {d}")
    print(f"The length of this cycle is {length}")

