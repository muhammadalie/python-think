import math
def hype(x,y):
	print 'x= ',x
	print 'y= ',y
	z=x*x + y*y
	return math.sqrt(z)

x=input("type x= ")
y=input("type y= ")

print hype(x,y)
