a=0
while a==0:
    nums=input('Enter 6 numbers between 1 and 9:')
    numslist=[]
    high=0
    low=9
    for x in range(0,len(nums)):
        numslist.append(nums[x])
    for x in range(0,len(numslist)):
        if int(numslist[x])>high:
            high = int(numslist[x])
        if int(numslist[x])<low:
            low = int(numslist[x])
    print('The difference between the largest and smallest numbers is '+str(high-low)+'.')
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
