x=str(input('Enter some things:'))
limit=2
x=list(x)
up=True
count=0
y=[]
for i in range(0,len(x)):
    if x[i].isalpha()==False:
        y.append(x[i])
    else:
        if up==True:
            y.append(x[i].upper())
            count+=1
            if count==limit:
                up=False
                count=0
        else:
            y.append(x[i].lower())
            count+=1
            if count==limit:
                up=True
                count=0    
y = ''.join(map(str, y)) 
print(y)
