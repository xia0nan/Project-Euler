"""
Author: Nan <xnone0104@gmail.com>

https://projecteuler.net/problem=23

[Non-Abundant Sums]
Problem 23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

"""
from math import isqrt
import time
import argparse


def get_proper_divisors_sum(n):
    """
    Returns the sum of proper divisors of a given number n.
    Using an optimized approach that only iterates up to the square root of n.
    """
    if n <= 1:
        return 0
        
    # Start with 1 as it's always a proper divisor
    divisors_sum = 1
    
    # Check divisors up to the square root of n
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            # Add both the divisor and its pair
            divisors_sum += i
            # Avoid adding the same divisor twice (in case of perfect squares)
            if i != n // i:
                divisors_sum += n // i
                
    return divisors_sum


def is_abundant(n):
    """
    Determines if a number n is abundant by checking if the sum
    of its proper divisors exceeds n.
    """
    return get_proper_divisors_sum(n) > n


def get_abundant_numbers(limit, debug=False):
    """
    Returns a list of all abundant numbers up to a given limit.
    """
    if debug:
        print(f"Finding abundant numbers up to {limit}...")
        start_time = time.time()
    
    abundant_nums = [n for n in range(12, limit + 1) if is_abundant(n)]
    
    if debug:
        end_time = time.time()
        print(f"Found {len(abundant_nums)} abundant numbers (time: {end_time - start_time:.2f}s)")
        print(f"First 10 abundant numbers: {abundant_nums[:10]}...")
    
    return abundant_nums


def get_abundant_sums(abundant_numbers, limit, debug=False):
    """
    Returns a set of numbers that can be expressed as the sum of two abundant numbers.
    Uses a set for O(1) lookups when determining non-abundant sums.
    """
    if debug:
        print(f"Generating sums of abundant numbers up to {limit}...")
        start_time = time.time()
    
    abundant_sums = set()
    count = 0
    
    # Generate all possible sums of two abundant numbers
    for i, a in enumerate(abundant_numbers):
        for b in abundant_numbers[i:]:  # Start from i to avoid duplicates
            sum_ab = a + b
            if sum_ab <= limit:
                abundant_sums.add(sum_ab)
                count += 1
                # Print progress for every million pairs processed
                if debug and count % 1000000 == 0:
                    print(f"Processed {count} pairs, found {len(abundant_sums)} unique sums")
            else:
                # If we exceed the limit, no need to continue with this a
                break
    
    if debug:
        end_time = time.time()
        print(f"Found {len(abundant_sums)} numbers expressible as sum of two abundant numbers")
        print(f"Time to generate sums: {end_time - start_time:.2f}s")
        
        # Sanity check: verify known cases
        print(f"Is 24 in abundant_sums? {24 in abundant_sums} (should be True)")
    
    return abundant_sums


def calculate_non_abundant_sum(limit, debug=False):
    """
    Finds the sum of all positive integers that cannot be written as the sum of two abundant numbers.
    """
    if debug:
        print(f"Starting calculation for limit {limit}...")
    
    abundant_numbers = get_abundant_numbers(limit, debug)
    abundant_sums = get_abundant_sums(abundant_numbers, limit, debug)
    
    if debug:
        print("Calculating sum of non-abundant sums...")
        start_time = time.time()
        
        # Testing small values to verify logic
        test_cases = [23, 24, 25]
        for test in test_cases:
            status = "cannot" if test not in abundant_sums else "can"
            print(f"{test} {status} be expressed as sum of two abundant numbers")
    
    total = sum(n for n in range(1, limit + 1) if n not in abundant_sums)
    
    if debug:
        end_time = time.time()
        print(f"Time to calculate final sum: {end_time - start_time:.2f}s")
    
    return total


def test_small_case():
    """
    Test function with a smaller limit to verify correctness.
    """
    print("\n=== RUNNING TEST WITH SMALL LIMIT ===")
    SMALL_LIMIT = 100
    
    # Manually verify some numbers
    for n in [12, 18, 20, 24, 30]:
        sum_of_divisors = get_proper_divisors_sum(n)
        status = "abundant" if sum_of_divisors > n else "not abundant"
        print(f"{n}: sum of divisors = {sum_of_divisors}, {status}")
    
    result = calculate_non_abundant_sum(SMALL_LIMIT, debug=True)
    print(f"Sum of non-abundant sums up to {SMALL_LIMIT}: {result}")
    print("=== TEST COMPLETE ===\n")


def main():
    """
    Main function to execute the solution.
    """
    parser = argparse.ArgumentParser(description='Solve Project Euler Problem 23')
    parser.add_argument('--test', action='store_true', help='Run test cases instead of the full problem')
    parser.add_argument('--debug', action='store_true', help='Show debug information')
    args = parser.parse_args()
    
    if args.test:
        test_small_case()
        return
    
    # Solve the actual problem
    LIMIT = 28123  # Given upper limit
    
    start_time = time.time()
    
    if args.debug:
        print("\n=== SOLVING ACTUAL PROBLEM ===")
    
    result = calculate_non_abundant_sum(LIMIT, args.debug)
    
    end_time = time.time()
    
    # Always print the final result
    print(f"Sum of all positive integers which cannot be written as the sum of two abundant numbers: {result}")
    
    if args.debug:
        print(f"Total execution time: {end_time - start_time:.2f}s")


if __name__ == "__main__":
    main()
