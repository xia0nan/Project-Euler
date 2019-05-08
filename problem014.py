"""
Author: Nan <xnone0104@gmail.com>

https://projecteuler.net/problem=14

[Longest Collatz sequence]

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""

# length = 0

# numdic = {}

# def check_length(num, count):
# 	global length
# 	if num == 1:
# 		length = count

# 	elif num % 2 == 0:
# 		num = num / 2
# 		check_length(num, count + 1)
# 	else:
# 		num = num * 3 + 1
# 		check_length(num, count + 1)



# def main():
# 	max_length = 0
# 	result = 0

# 	for i in xrange(1, 1000001):
# 		check_length(i, count=1)
# 		if length > max_length:
# 			max_length = length
# 			result = i
# 	print "result", result, "max", max_length


# if __name__ == '__main__':
# 	main()


# # Soln 1: 
# collatz = {1:1}
# def Collatz(n):
#     global collatz
#     if not collatz.has_key(n):
#         if n%2 == 0:
#             collatz[n] = Collatz(n/2) + 1
#         else:
#             collatz[n] = Collatz(3*n + 1) + 1
#     return collatz[n]

# for j in range(1000000,0,-1):
#     Collatz(j)

# print collatz.keys()[collatz.values().index(max(collatz.values()))]    


# # Soln 2:
# def next(n):
#     if n % 2:
#         return 3 * n + 1
#     else:
#         return n / 2

# class ChainCache:
#     def __init__(self):
#         self.cache = {}

#     def __call__(self, n):
#         if n == 1:
#             return 1
#         elif n in self.cache:
#             return self.cache[n]
#         else:
#             c = self.__call__(next(n))
#             self.cache[n] = c + 1
#             return c + 1

# chainlen = ChainCache()

# def maxlen(x):
#     m = 0
#     v = 0
#     for i in range(1, x):
#         l = chainlen(i)
#         if l > m:
#             m = l
#             v = i
#     return v, m

# print maxlen(1000000)