x=str(input('Enter some things:'))
x=list(x)
count=0
limit=2
up=True
y=[]
for i in range(0,len(x)):
    if x[i].isalpha()==False:
        if x[i]=='"' or x[i]=="'":
            y.append(x[i])
        else:
            if i+1<len(x):
                if x[i+1].isalpha()==False:
                    y.append(x[i])
                    count+=1    
                    if count==limit:
                        if up==True:
                            up=False
                        else:
                           up=True
                        count=0
                else:
                    count+=1
                    if count==limit:
                        if up==True:
                            up=False
                        else:
                           up=True
                        count=0
                    y.append(x[i])
    else:
        if up==True:
            y.append(x[i].upper())
        else:
            y.append(x[i].lower())
y = ''.join(map(str, y)) 
print(y)
