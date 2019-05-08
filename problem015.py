"""
Author: Nan <xnone0104@gmail.com>

https://projecteuler.net/problem=15

[Lattice paths]

Starting in the top left corner of a 2×2 grid, 
and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?

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

