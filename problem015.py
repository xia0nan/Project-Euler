__author__ = "xiaonan"

"""
https://projecteuler.net/problem=15
"""


def count_path(x):
	numlist = [1] * (x + 1)
	n = 1
	while n < x:
		for i in xrange(x + 1):
			for j in xrange(i + 1, x + 1):
				numlist[i] += numlist[j]
		n += 1
	return sum(numlist)


def main():
	count_path(20)
		

if __name__ == '__main__':
	main()

