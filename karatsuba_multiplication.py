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

print karatsuba_multiplication(1685287499328328297814655639278583667919355849391453456921116729,\
	7114192848577754587969744626558571536728983167954552999895348492)