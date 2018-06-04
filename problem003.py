__author__ = "xiaonan"

"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
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


def check_prime(number):
	sqroot = int(number**0.5)
	for i in reversed(xrange(sqroot)):
		if number % i == 0 and isprime(i):
			print "found", i
			return -1

if __name__ == '__main__':
	check_prime(600851475143)