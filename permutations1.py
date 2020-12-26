from itertools import permutations
a=0
while a==0:
    list1=input('Enter a list of numbers:')
    list2=[]
    for x in range(0,len(list1)):
        list2.append(int(list1[x]))
    print(list2)
    perms=permutations(list2)
    for i in list(perms):
        print(i)
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


