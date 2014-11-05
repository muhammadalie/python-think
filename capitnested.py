def capall(t):
	res = []
	j = []
	for s in t:
		if type(s)!=list:
        		res.append(s.capitalize())
		else:
			for i in s:
				j.append(i.capitalize())
			res.append(j)
	return res

t=input('list: ')
print capall(t)
