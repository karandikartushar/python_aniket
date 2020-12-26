import random
def board(location,player):
    ladders={5:8,12:55,9:84,20:99,11:98}
    snakes={6:2,56:15,67:64,54:46,90:73}
    if location in ladders:
        print('Congratulations '+player+'!You got a ladder!')
        return ladders[location]
    elif location in snakes:
        print('Oh no '+player+'!You got a snake!')
        return snakes[location]
    else:
        return location
a=0
while a==0:
    location1=1
    location2=1
    print('Welcome to snakes and ladders!')
    player1=input('Player 1:Enter your name:')
    player2=input('Player 2:Enter your name:')
    if player1==player2:
        player1='player 1'
        player2='player 2'
    while location1<100 and location2<100:
        print('The postition of '+str(player1)+' is '+str(location1)+'.')
        print('The postition of '+str(player2)+' is '+str(location2)+'.')
        x=random.randint(1,6)
        print('The number on the dice for '+str(player1)+' is '+str(x)+'.')
        location1=board(location1+x,player1)
        print('The postition of '+str(player1)+' is '+str(location1)+'.')
        if location1>=100:
            break
        y=random.randint(1,6)
        print('The number on the dice for '+str(player2)+' is '+str(y)+'.')
        location2=board(location2+y,player2)
        print('The postition of '+str(player2)+' is '+str(location2)+'.')
    if location1>=100:
        print('Congratulations '+str(player1)+'!You won!')
    elif location2>=100:
        print('Congratulations '+str(player2)+'!You won!')
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
