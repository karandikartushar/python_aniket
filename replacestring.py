word=input('Enter a word:')
word1=[]
compare=str(word[0])
for i in range(0,len(word)):
    word1.append(word[i])
for i in range(1,len(word)):
    if word1[i]==compare:
        word1[i]='$'
word=str(word1)
print(word)
    
