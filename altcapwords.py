x=str(input('Enter some things:'))
x=list(x)
z=0
a=2
y=[]
for i in range(0,len(x)):
    if x[i].isalpha()==False:
        if x[i]!="'" or '"':
            if a==0:
                a+=1
            else:   
                a-=1
        y.append(x[i])
    else:
        if a==1:
            y.append(x[i].upper())
        else:
            y.append(x[i].lower())
    
    
y = ''.join(map(str, y)) 
print(y)
