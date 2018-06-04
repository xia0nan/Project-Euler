__author__ = "xiaonan"

"""
Solution for: https://projecteuler.net/problem=4
"""

import sys

def reverseNum(number):
	return int(str(number)[::-1])


def isPalindrome(number):
	if number == reverseNum(number):
		return True
	return False


def main():
	result = 0
	for i in reversed(xrange(999)):
		for j in reversed(xrange(999)):
			if isPalindrome(i*j):
				if result < i * j:
					result = i * j
					print "%d = %d * %d" % (result, i, j)
				break
				

if __name__ == '__main__':
	main()