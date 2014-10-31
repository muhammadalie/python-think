def fact(n):
	if type(n)==int: 
		print 'n is not integer'
		return None 
	elif 0<=n<=2:return n
	elif n<0: 
		print 'not defined,number is negative'
		return None 
	return n*fact(n-1)

n=input('type your number: ')
print 'the factorial is  ',fact(n)
