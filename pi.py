import math
x=(math.factorial(4*k)*(1103+26390*k))/(((math.factorial(k))**4)*(396**(4*k)))	 
k=0
while  k>=0:
	x=(math.factorial(4*k)*(1103+26390*k))/(((math.factorial(k))**4)*(396**(4*k)))
	if(x<10**-15):break
	
