def dic(a):
	a=open(a)
	j=0
	b=(a.read()).split()
	abc=dict()
	for i in b:
		abc[i]=j
		j+=1	
	return abc

a=input('file: ')
print dic(a)

