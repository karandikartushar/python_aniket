a=0
while a==0:
    x=input('Which is the better programing language python or java:')
    list1=[]
    y=x.split()
    for i in range(0,len(y)):
        if y[i]=='python':
            list1.insert(i,'java')
        elif y[i]=='java':
            list1.insert(i,'python')
        else:
            list1.insert(i,y[i])
    print(list1)
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
