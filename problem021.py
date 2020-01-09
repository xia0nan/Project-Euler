"""
Author: Nan <xnone0104@gmail.com>

https://projecteuler.net/problem=21

[Amicable numbers]

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, 
where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""

def proper_divisors(num):
	# return proper divisors of a number
	result = list()
	for i in range(1, int(num / 2) + 1):
		if num % i == 0:
			result.append(i)
	return result

def d(number):
	result = proper_divisors(number)
	out = sum(result)
	return out

def main():
	bound = 10000
	results = []
	for a in range(bound + 1):
		b = d(a)
		if (b != a) and (d(b) == a):
			results.append(a)
			results.append(b)
	print(sum(results)//2)  # each pair shows up twice

def test():
	print(d(220))  # 284
	print(d(284))  # 220

if __name__ == '__main__':
	main()
	# test()

		

