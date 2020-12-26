word=['c','o','n','c','e','n','t','r','a','t','i','o','n']
word1=['','o','','','e','','','','a','','i','o','']
lives=5
while lives>0:
    la=0
    print(word1)
    print('lives are ',lives)
    letter=input('Enter a letter:')
    while len(letter)>1:
        letter=input('Enter a letter:')
    for x in range(0,len(word)):
        if id(letter)==id(word[x]):
            word1[x]=letter
            la+=1
    if la ==0:
        lives-=1
    for x in range(0,len(word)):
        if la==4:
            lives=-1
if lives>0 or lives<0:
    print('Congrats!You won!')
else:
    print('Sorry.You lost.')
