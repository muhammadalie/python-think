def find(word, letter,index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

w=input('type a word:  ')
l=input('type letter to find: ')
i=input('type postion from:  ' )
print find(w,l,i)
