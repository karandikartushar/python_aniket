a=0
while a==0:
    num1=int(input('Enter a numbers:'))
    num2=int(input('Enter a numbers:'))
    num3=int(input('Enter a numbers:'))
    list1=[]
    list1.append(num1)
    list1.append(num2)
    list1.append(num3)
    list1.sort()
    hypotenuse=list1[-1]
    if list1[0]**2+list1[1]**2==hypotenuse**2:
        print('The triangle is a right angled triangle')
    else:
        print('The triangle is not a right angled triangle')
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
