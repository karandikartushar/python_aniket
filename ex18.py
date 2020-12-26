import random
def main():
    a=str(random.randrange(999,9999))
    c=input('enter a number:')
    while c != a:
        cow=0
        bull=0
        if a[0]==c[0]:
           cow+=1
        if a[0]==c[1]:
            bull+=1
        if a[0]==c[2]:
            bull+=1
        if a[0]==c[3]:
            bull+=1
        if a[1]==c[0]:
            bull+=1
        if a[1]==c[1]:
            cow+=1 
        if a[1]==c[2]:
            bull+=1
        if a[1]==c[3]:
            bull+=1
        if a[2]==c[0]:
            bull+=1
        if a[2]==c[1]:
            bull+=1
        if a[2]==c[2]:
            cow+=1 
        if a[2]==c[3]:
            bull+=1
        if a[3]==c[0]:
           bull+=1
        if a[3]==c[1]:
            bull+=1
        if a[3]==c[2]:
            bull+=1 
        if a[3]==c[3]:
            cow+=1
        if c=='quit':
            break
        print(cow,'cows',bull,'bulls')
        c=str(int(input('enter a number:')))
    print('Got it!')
    
print('Welcome to the cows and bulls game!')
d='yes'
while d=='yes':
    main()
    d=input('Do you want to play again?')
print('Bye Bye')
