def rot(a,n):
	s=''
	for i in a:
		k=ord(i)
		g=k+n
		s+=chr(g)
	return s

a=raw_input('word:  ')
n=input('shift: ')
print n,' times shifted word is ',rot(a,n)
