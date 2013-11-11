# This program converts the fractional part of a decimal number to the fractional part of a binary number. Note that parameter to the function must be a string. For example, "07" shows the fractional part of "0.07" in binary. The limit is the number of decimal places to show

limit = 53


def convert_fraction(n):
	l = len(n)
	number = int(n)
	cut = 5 * 10 ** (l-1)
	result_str = ''
	for i in range(limit):
		number *= 10
		cut *= 10
		if number > cut:
			result_str += '1'
			number -= cut
			cut /= 2
		if number < cut:
			result_str += '0'
			cut /= 2
	return result_str
print(convert_fraction('07'))

