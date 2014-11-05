def hist(a):
        b=dict()
        for i in a:
                b[i]=1+b.get(i,0)

        return b

def rvlk(d, v):
	c=[]
	
    	for k in d:
        	if d[k] == v:
        		c.append(k)
	if v in d.values():return c 	
   	else:raise ValueError, 'this value not appear in this dictionary'

a=input('string: ')
h=hist(a)
b=input('value: ')
print rvlk(h,b)
