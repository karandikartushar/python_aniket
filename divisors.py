a=0
while a==0:
    def divisors(num):
        for x in range(1,(num+1)):
            if num%x==0:
                factors.append(x)
    factors=[]
    divisors(int(input('Enter a number:')))
    print('The number of divisors is '+str(len(factors))+'.')
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
