a=input('enter a number.Type done to stop:')
b=[]
e=0
while a!='done':
    a=int(a)
    b.append(a)
    a=input('enter a number.Type done to stop:')
c=int(input('Enter a number:'))
for num in b:
    e=num*c+e
print(e)


    
