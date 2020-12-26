a=0
while a==0:
    NumStr=input('Enter some numbers:')
    for i in range(0,len(NumStr)):
        if NumStr[i] not type(int):
            print('Invalid input')
            break
    NumList=[]
    for x in range(0,len(NumStr)):
        NumList.append(NumStr[x])
    NumList.sort()
    if len(NumList)%2==0:
        Median=len(NumList)/2+(len(NumList)/2+1)/2
    else:
        Median=len(NumList)/2+0.5
    print('The median is '+str(Median)+'.')
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
