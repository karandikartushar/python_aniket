play=1
while play==1:
    x=int(input('Enter a number:'))
    if x>1:
        if x==2:
            print('This number is prime')
            play=int(input('Play again?1 for yes and 2 for no:'))
            continue
        z=2
        while x%z != 0:
            z+=1
        if z==x:
            print('This number is prime')
            play=int(input('Play again?1 for yes and 2 for no:'))
        else:
            print('The number is not prime.')
            play=int(input('Play again?1 for yes and 2 for no:'))
    else:
        print('Number is not prime.')
        play=int(input('Play again?1 for yes and 2 for no:'))
