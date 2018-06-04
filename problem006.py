__author__ = "xiaonan"
"""
Solution for: https://projecteuler.net/problem=6
"""

def sum_of_square(number):
	result = 0
	for i in xrange(number):
		result += (i+1)**2
	print "sum_of_square", result
	return result


def square_of_sum(number):
	result = 0
	for i in xrange(number):
		result += i + 1
	print "square_of_sum", result ** 2
	return result ** 2

def main():
	print square_of_sum(100) - sum_of_square(100)


if __name__ == '__main__':
	main()