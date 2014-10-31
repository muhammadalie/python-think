def pal(a):
	if a==a[::-1]:return True
	return False	

a=raw_input('enter the string: ')
print pal(a)
