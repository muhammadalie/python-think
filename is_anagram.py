def anagram(a,b):
	m=list(a)
	n=list(b)
	m.sort()
	n.sort()
	if m==n:return True
	return False

a=input('first word: ')
b=input('second word: ')
print anagram(a,b)
