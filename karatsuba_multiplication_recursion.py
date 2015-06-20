def karatsuba_multiplication(x, y):
	x_size = len((str(x)))
	y_size = len((str(y)))
	
	x1 = int((str(x))[:(x_size / 2)])
	x2 = int((str(x))[(x_size / 2):])
	y1 = int((str(y))[:(y_size / 2)])
	y2 = int((str(y))[(y_size / 2):])

	n = x_size if x_size > y_size else y_size

	mult = ((10**n)*x1*y1) + ((10**(n / 2))*((x1+x2)*(y1+y2) - x1*y1 - x2*y2)) + x2*y2
	return mult


def multiplication(num1, num2, counter): 
	if len(str(num1)) == 1 and len(str(num2)) == 1:
		return (long(num1) * long(num2), counter)
	else:
		n = max(len(str(num1)), len(str(num2)))

		if len(str(num1)) % 2 != 0 or len(str(num2)) % 2 != 0:
			num1 = (n + 1 - len(str(num1))) * "0" + str(num1) if n % 2 != 0 else (n - len(str(num1))) * "0" + str(num1)
			num2 = (n + 1 - len(str(num2))) * "0" + str(num2) if n % 2 != 0 else (n - len(str(num2))) * "0" + str(num2)
		n = len(str(num2))

		a = str(num1)[:n / 2]
		b = str(num1)[n / 2:]
		c = str(num2)[:n / 2]
		d = str(num2)[n / 2:]

		ac, counter = multiplication(long(a), long(c), counter)
		bd, counter = multiplication (long(b), long(d), counter)
		x, counter = multiplication(long(a) + long(b), long(c) + long(d), counter)

		adcb = x - ac - bd
		if adcb == 12:
			counter += 1
		
		print "ac %d" % ac
		print "adcb %d" % adcb
		print "bd %d" % bd

		return (((10 ** n) * ac) + ((10 ** (n / 2)) * adcb) + bd, counter)


counter = 0
# a = 1685287499328328297814655639278583667919355849391453456921116729
# b = 7114192848577754587969744626558571536728983167954552999895348492	
# right_res = 11989460275519080564894036768322865785999566885539505969749975204962718118914971586072960191064507745920086993438529097266122668
a = 71611955325935479159397713213124
b = 93567726499788166681348352945366
right_res = 6700567850052179472481148730882040129649508491917840721086183384


res = multiplication(a, b, counter)
hues = karatsuba_multiplication(a, b)

if hues == right_res:
	print True

if res[0] == right_res:
	print  True

print res[1]
			