def hist(a):
	b=dict()
	for i in a:
		if i in b:
			b[i]+=1
		else:
			b[i]=1	
	return b

a=input('string: ')
print hist(a)
