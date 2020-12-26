a=0
while a==0:
    c=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    d=[]
    e=[]
    f=[]
    while c!=1:
        for x in range(0,int(c)):
            if c%x==0:
                d.append(x)
                c=c/x
                break
    while b!=1:        
        for x in range(0,int(b)):
            if b%x==0:
                e.append(x)
                b=b/x
                break
    
    for x in range(0,len(d)):
        if d[x] in e:
            e.remove(d[x])
    temp=e+d
    g=1
    for x in range(0,len(temp)):
        g=g*temp[x]
    print('The LCM is '+str(g)+'.')
    z=input('Do you want to play again?Y or y for yes and N or n for no:')
    if z=='y':
        a+=0
    elif z=='Y':
        a+=0
    elif z=='N':
        a+1
    elif z=='n':
        a+=1
    else:
        print('Invalid input.Sorry.')
        a+=1
print('Game over.Thanks for playing!')
