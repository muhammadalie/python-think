import math

def sqroot(a):
        x=5.0
        while True:
                y = (x + a/x) / 2
                if y==x:
                        return x
                x=y

def prints(n):
	a=1
	while a<n:
		x=sqroot(a)
		y=math.sqrt(a)
		z=abs(x-y)
		print a,':','\t',x,'\t',y,'\t',z
		a+=1

a=input('limit: ')
prints(a)
