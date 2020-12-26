import random
print('Enter a number between 0 and 100')
num=50
print('My number is ',num,'.')
z=input('Too high or too low or correct?:')
guess=0
while z != num:
    if z=='too high':
        num-=1
        print('My number is ',num,'.')
        z=input('Too high or too low or correct?:')
        guess+=1
    if z=='too low':
        num+=1
        print('My number is ',num,'.')
        z=input('Too high or too low or correct?:')
        guess+=1
    if z=='correct':
        break

print('Got it!')
print('It took you ',guess,' tries.')
