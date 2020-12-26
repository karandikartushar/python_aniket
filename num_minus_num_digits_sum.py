a=0
while a==0:
    num=int(input('Enter a number:'))
    count=0
    while num!=0:
        numlist=[]
        for x in range(0,len(str(num))):
            numlist.append(str(num)[x])
        num3=0
        for i in range(0,len(numlist)):
            num3+=int(numlist[i])
        print('The sum of the digits of '+str(num)+' is '+str(num3)+'.')
        print(str(num)+' - '+str(num3)+' is '+str(num-num3)+'.')
        num-=num3
        count=count+1
    print('count ' + str(count))
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
print('Game over.Thanks for playing!')
