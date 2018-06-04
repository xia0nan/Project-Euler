__author__ = "xiaonan"

"""
https://projecteuler.net/problem=16
"""

if __name__ == '__main__':
	result = 0
	number = 2 ** 1000

	num_list = list(str(number))
	for num in num_list:
		result += int(num)
	print result