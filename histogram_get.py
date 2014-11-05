def hist(a):
        b=dict()
        for i in a:
		b[i]=1+b.get(i,0)
		
        return b
def printh(h):
	a=[]
	for c in h:
		a.append(c)
	a.sort()
        for i in a:
		print i,h[i]

a=input('string: ')
b=hist(a)
print b
print printh(b)
