def count(word,letter):
	
	count = 0
	for i in word:
    		if i == letter:
        		count = count + 1
	return count

w=input('word: ')
l=input('letter: ')
print count(w,l)
