a=0
while a==0:
    num=int(input('Enter the number of fibbonacci numbers:'))
    fibbonacci=[0,1,2]
    while len(fibbonacci)<num:
        fibbonacci.append(int(fibbonacci[-1])+int(fibbonacci[-2]))
    print(fibbonacci)
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
        a+=1
print('Game over.Thanks for playing!')
