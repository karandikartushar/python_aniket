a=0
while a==0:
    b=int(input('Enter a number:'))
    primes=[]
    num=1
    count=0
    finalnum=0
    while len(primes)!=b:
        count-=count
        num+=1
        for x in range(2,num+1):
            if num%x==0:
                count+=1
        if count==1:
            primes.append(num)
    for x in range(0,len(primes)):
        finalnum+=primes[x]
    print(primes)
    print('The sum of the primes is '+str(finalnum))
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
            
