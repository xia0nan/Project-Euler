__author__ = "xiaonan"

"""
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def divisible(number):
	for i in range(11, 21):
		if number % i != 0:
			return False
	return True


def main():
	step = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
	i = step

	while not divisible(i):
		i += step
		print "trying", i
	print i


if __name__ == '__main__':
	main()