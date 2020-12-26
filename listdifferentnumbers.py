a=0
while a==0:
    list1=input('Enter a list of numbers:')
    y=0
    b=0
    list2=[]
    for x in range(0,len(list1)):
        list2.append(int(list1[x]))           
    for x in range(0,len(list2)):
        for i in range(x+1,len(list2)):
            if list2[x]==list2[i]:
                b+=1
                break
            else:
                y+=1
    if b==0:
        print('The list has no repeating numbers')
    else:
        print('The list has repeating numbers.')
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
