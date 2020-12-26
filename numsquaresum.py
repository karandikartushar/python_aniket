a=0
while a==0:
    num=int(input('Enter a number:'))
    c=0
    for x in range(1,num):
        b=x**3
        c+=b
    print(c)
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

    
