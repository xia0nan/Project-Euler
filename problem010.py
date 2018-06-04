__author__ = "xiaonan"

"""
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def isprime(number):
	if number < 2:
		return False
	elif number == 2 or number == 3:
		return True
	elif number % 2 == 0 or number % 3 == 0:
		return False
	i = 5
	while i * i <= number:
		if number % i == 0 or number % (i + 2) == 0:
			return False
		i += 6
	return True


def sumPrime(number):
	result = 0
	for i in xrange(number):
		if isprime(i):
			result += i
	print result


def main():
	sumPrime(2000000)


if __name__ == '__main__':
	main()