a=input('enter rock,paper or scissors.type end to end:')
b=input('enter rock,paper or scissors.type end to end:')
while a!='end' and b != 'end':
    if a=='rock'and b=='scissors':
        print('Player 1 won!')
        a=input('enter rock,paper or scissors.type quit to quit:')
        b=input('enter rock,paper or scissors.type quit to quit:')
    elif a=='rock'and b=='paper':
        print('Player 2 won!')
        a=input('enter rock,paper or scissors.type quit to quit:')
        b=input('enter rock,paper or scissors.type quit to quit:')
    elif a=='rock'and b=='rock':
        print('Tie!')
        a=input('enter rock,paper or scissors.type quit to quit:')
        b=input('enter rock,paper or scissors.type quit to quit:')
    elif a=='scissors'and b=='scissors':
        print('Tie!')
        a=input('enter rock,paper or scissors.type quit to quit:')
        b=input('enter rock,paper or scissors.type quit to quit:')
    elif a=='scissors'and b=='paper':
        print('Player 1 won!')
        a=input('enter rock,paper or scissors.type quit to quit:')
        b=input('enter rock,paper or scissors.type quit to quit:')
    elif a=='scissors'and b=='rock':
        print('Player 2 won!')
        a=input('enter rock,paper or scissors.type quit to quit:')
        b=input('enter rock,paper or scissors.type quit to quit:')
    elif a=='paper'and b=='scissors':
        print('Player 2 won!')
        a=input('enter rock,paper or scissors.type quit to quit:')
        b=input('enter rock,paper or scissors.type quit to quit:')
    elif a=='paper'and b=='paper':
        print('Tie!')
        a=input('enter rock,paper or scissors.type quit to quit:')
        b=input('enter rock,paper or scissors.type quit to quit:')
    elif a=='paper'and b=='rock':
        print('Player 1 won!')
        a=input('enter rock,paper or scissors.type quit to quit:')
        b=input('enter rock,paper or scissors.type quit to quit:')
print('thanks for playing')
