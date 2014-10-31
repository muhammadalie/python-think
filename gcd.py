def gcd(a,b): 
	if a%b==0:return b
	elif b%a==0:return a
	if(b>a):
		return gcd(a,b%a)
	elif(a>b):return gcd(a,a%b)

	
a=input('first number: ')
b=input('second number: ')
print 'gcd of ',a,' and ', b ,' is ',gcd(a,b)
