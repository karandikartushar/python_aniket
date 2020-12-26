players=[]
for y in range(1,3):
    players.append({'name':'','score':0,'backpack':[]})
    players[y-1]['name']=input('Enter name of player '+str(y)+':')
    for x in range(1,5):
        players[y-1]['backpack'].append(input('Enter 1 thing for player'+str (y)+':'))
z='yes'
while z!='no':
    c=1
    for a in range(2):
        b=input('Player '+str(a+1)+' guess:')
        if b in players[c]['backpack']:
            print('Congratulations!You guessed correct')
            players[a]['score']+=1
        else:
            print('Wrong guess.')
        c=0
    print('player 1 score='+str(players[0]['score'])+'.')
    print('player 2 score='+str(players[1]['score'])+'.')
    if players[0]['score']>players[1]['score']:
        print('Player 1 wins!')
        z=input('Do you want to play again:')
    if players[0]['score']<players[1]['score']:
        print('Player 2 wins!')
        z=input('Do you want to play again:')
    if players[0]['score']==players[1]['score']:
        print('Tie!')
        z=input('Do you want to play again:')
    
print('Game over!')
print('Thanks for playing!')

