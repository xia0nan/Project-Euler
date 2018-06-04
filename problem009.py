__author__ = "xiaonan"

"""
Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def main():
	for i in xrange(1000):
		for j in xrange(1000):
			if i + j < 500:
				continue
			elif (i*i + j*j)**0.5 % 1 == 0 and (i*i + j*j)**0.5 == 1000 - i - j:
				print i, j, (i*i + j*j)**0.5
				print i * j * (i*i + j*j)**0.5


if __name__ == '__main__':
	main()