__author__ = "xiaonan"


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


def main():
	count = 1
	i = 2
	while count <= 10001:
		if isprime(i):
			count += 1
		i += 1
	print '%d is %dth prime' % (i - 1, count - 1)


if __name__ == '__main__':
	main()