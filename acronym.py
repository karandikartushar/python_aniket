x=input('Enter a sentence:')
x=x.upper()
x=x.split()
letters=[]
for word in x: 
    letters.append(word[0])
    
print('the acronym of your sentence is',''.join(letters),'.')
