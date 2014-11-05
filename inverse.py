def hist(a):
        b=dict()
        for i in a:
                b[i]=1+b.get(i,0)

        return b

def invert(d):
   	inverse = dict()
  	for key in d:
        	val = d[key]
        	if val not in inverse:
        	    inverse[val] = [key]
        	else:
        	    inverse[val].append(key)
    	return inverse


a=input('list: ')
h=hist(a)
print h
print invert(h)
