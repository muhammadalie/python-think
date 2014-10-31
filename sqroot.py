def sqroot(a):
	x=5.0
	while True:
    		y = (x + a/x) / 2
   		if y==x:
			return x
    		x=y

a=input('number: ')
print sqroot(a)
