def sqr(n):return n*n
	
def powr(x,y):
	if (y<=0): return 1 	
	return sqr(x)*powr(x,y-1)
