"""
Author: Nan <xnone0104@gmail.com>

https://projecteuler.net/problem=17

"""

def num2word(number):
	numdict = {  
		0:'zero',
		1:'one',
		2:'two',
		3:'three',
		4:'four',
		5:'five',
		6:'six',
		7:'seven',
		8:'eight',
		9:'nine',
		10:'ten',
		11:'eleven',
		12:'twelve',
		13:'thirteen',
		14:'fourteen',
		15:'fifteen',
		16:'sixteen',
		17:'seventeen',
		18:'eighteen',
		19:'nineteen',
		20:'twenty',
		30:'thirty',
		40:'forty',
		50:'fifty',
		60:'sixty',
		70:'seventy',
		80:'eighty',
		90:'ninety'
	}

	assert number > 0

	if number < 21:
		return numdict[number]
	elif number < 100:
		if number % 10 == 0:
			return numdict[number]
		else:
			return numdict[number / 10 * 10] + '-' + numdict[number % 10]
	elif number < 1000:
		if number % 100 == 0:
			return numdict[number / 100] + ' hundred'
		else:
			return numdict[number / 100] + ' hundred and ' + num2word(number % 100)
	elif number == 1000:
		return "one thousand"
	else:
		raise AssertionError('num is too large: %s' % str(number))


def countwords(phrase):
	phrase = phrase.replace(' ', '')
	phrase = phrase.replace('-', '')
	print phrase
	print "len", len(phrase)
	return len(phrase)


def main():
	wordsum = 0
	for i in range(1, 1001):
		print i
		phrase = num2word(i)
		print phrase
		wordsum += countwords(phrase)
		print "sum now", wordsum
	print wordsum


if __name__ == '__main__':
	main()