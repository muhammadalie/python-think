def issorted(a):
	c = []
	for i in a:
		c.append(i)
	c.sort()
	if a==c:
		return True
	return False

a=input('list: ')
print issorted(a)
		
