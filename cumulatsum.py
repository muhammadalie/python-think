def cumu(s):
	k = []
	t=0
	for i in s:
		t+=i
		k.append(t)
	return k

s=input('list: ')
print cumu(s)
	
