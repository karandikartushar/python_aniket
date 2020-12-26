a=input('enter a number.Type done to stop:')
b=[]
d=[]
e=0
while a!='done':
    a=int(a)
    b.append(a)
    a=input('enter a number.Type done to stop:')
c=input('enter a number.Type done to stop:')
while c!='done':
    c=int(c)
    d.append(c)
    c=input('enter a number.Type done to stop:')
for i in d:
    for num in b:
        
        #num=num*i
        #e=e+num
        e=num*i+e

print(e)


    
