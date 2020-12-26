a=0
while a==0:
    number=input('Enter a number:')
    num2=number[::-1]
    while number!=num2:
        print(number)
        number=int(number)
        num2=int(num2)
        number+=num2
        number=str(number)
        num2=str(num2)
        num2=number[::-1]
    print(str(number))
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
