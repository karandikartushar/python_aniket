a=0
while a==0:
    x=input("Enter a number:")
    x=list(x)
    y=len(x)
    z=set(x)
    b=len(z)
    if y==b:
        print('True.No repeating digits')
        z=input('Do you want to play again?Y or y for yes and N or n for no:')
        if z=='y':
            a=a+0
        elif z=='Y':
            a=a+0
        elif z=='N':
            print('Game over')
            break
        elif z=='n':
            print('Game over')
            break
        else:
            print('Invalid input.Sorry.Game over.')
            break
    else:
        print('False.Repeating digits exist.')
        z=input('Do you want to play again?Y or y  for yes and N or n for no:')
        if z=='y':
            a=a+0
        elif z=='Y':
            a=a+0
        elif z=='N':
            print('Game over')
            break
        elif z=='n':
            print('Game over')
            break
        else:
            print('Invalid input.Sorry.Game over.')
            break
print('Thanks for playing!')
    
