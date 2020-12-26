x=str(input('Enter some things:'))
x=list(x)
z=0
a=2
b=0
c=1
y=[]
for i in range(0,len(x)):
    if x[i].isalpha()==False:
        b+=1
        c+=1
        y.append(x[i])
    else:
        if b<=len(x)-2:
            y.append(x[b].upper())
            b+=2                  
        if c<=len(x)-2:           
            y.append(x[c].upper())
            c+=2
        if b<=len(x)-2:
            y.append(x[b].lower())
            b+=2
        if c<=len(x)-2:
            y.append(x[c].lower())
            c+=2
    
y = ''.join(map(str, y)) 
print(y)
