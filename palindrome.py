def pal(a):
	if len(a)<=1: return True
	elif a[0]==a[-1]:
		return pal(a[1:-1])
	else:return False

a=raw_input('type a word:  ')
print pal(a)
