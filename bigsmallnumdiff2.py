a=0
while a==0:
    nums=input('Enter 6 numbers between and 9:')
    numlist=[]
    for x in range(0,len(nums)):
        numlist.append(nums[x])
    print(numlist)
    ascending=(sorted(numlist,reverse=False))
    descending=(sorted(numlist,reverse=True))
    print(ascending)
    print(descending)
    ascending=int("".join(map(str, ascending))) 
    descending=int("".join(map(str, descending))) 
    print('The highest number is '+str(descending)+' and the lowest number is '+str(ascending)+' and their difference is '+str(int(descending)-int(ascending))+'.')
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
