def fun(f,s,m):
	n=0
	while(n>=0 and n<=m):
		if(n%5)==0:
			print f(m)
			n+=1
		else:
			print s(m)
			n+=1
	

def f(m):
	n=0
	c=''
	while(n>=0 and n<=m):
		if (n%5)==0:
			b='+'
			c=c+b
			n+=1
		else:
			b=' -'
			c=c+b
			n+=1
	return c

def s(m):
	n=0
        c=''
        while(n>=0 and n<=m):
                if (n%5)==0:
                        b='/'
                        c=c+b 
                        n+=1
                else:
                        b='  '
                        c=c+b 
                        n+=1
        return c

	
fun(f,s,10)
