a=0
while a==0:
    name=input('Enter your name:')
    age=int(input('Enter your age:'))
    year=int(input('Enter the current year:'))
    if age<100:
        b=str((100-age)+year)
        print(''+name+',you will be 100 years old in year '+b+'.')
    elif age==100:
        print(''+name+',you are 100 years old in year '+year+'.')
    elif age>100:
        b=str((100-age)+year)
        print(''+name+',you were 100 years old in year '+b+'.')
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
    
