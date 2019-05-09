# -*- coding: utf-8 -*-

"""
Author: Nan <xnone0104@gmail.com>

https://projecteuler.net/problem=20

[Factorial digit sum]

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""

import math

def factorial(n):
	fac = 1
	for i in range(n):
		fac *= i+1
	return fac

def factorial_digit_sum(fac):
	result = 0
	for i in str(fac):
		result += int(i)
	return result

fac = factorial(100)
result = factorial_digit_sum(fac)

print(result)