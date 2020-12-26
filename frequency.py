x=input('Enter a sentence:')
b={}
for i in range(0,len(x)):
    if x[i] in b:
        b[x[i]]+=1
    else:
        b[str(x[i])]=1
print(b)
