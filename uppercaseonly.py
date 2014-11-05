def onlyupper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

t=input('list: ')
print onlyupper(t)
