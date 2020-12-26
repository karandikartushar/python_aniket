a=0
while a==0:
    num1=int(input('Enter the first number:'))
    num2=int(input('Enter the second number:'))
    if num1>num2:
        highnum=num1
    else:
        highnum=num2
    for x in range(2,highnum+1):
        if num1%x==0 and num2%x==0:
            hcf=x
    print('hcf'+str(hcf)+'')
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
