def remove(a):
	b=[]
	for i in range(len(a)):
		if a[i] not in b:
			b.append(a[i])
				
	return b

a=input('list: ')
print remove(a)	 
