def middle(a):
	x=[]
	for i in range(1,len(a)-1):
		x.append(a[i])
	return x

a=input('list: ')
print middle(a)
