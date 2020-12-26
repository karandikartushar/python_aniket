import re 
x=str(input('Enter some things:'))
x=list(x)
z=0
a=2
y=[]
for i in range(0,len(x)):
    if x[i].isalpha()==False:
        a+=1
        if a%2==1:
            z+=1
        else:
            z=0
        y.append(x[i])
    else: 
        if i%2==z:
            y.append(x[i].upper())
        else:
            y.append(x[i].lower())
    
    
y = ''.join(map(str, y)) 
print(y)




  
