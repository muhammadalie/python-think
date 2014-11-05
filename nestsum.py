def sum(a):
	t=0
	for i in a:
		if type(i)==int:
			t+=i
		else:
			for j in i:
				t+=j
	return t

a=input('array')
print sum(a) 
		
	
