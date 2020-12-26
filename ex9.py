import random

def play_game():
    x=random.randint(1,10)
    count=0
    z=float(input('enter a number from 1 to 9.'))
    count=count+1
    while z != x: 
      if z>x:
        print('to high')
        z=float(input('enter a number from 1 to 9.:'))
        count=count+1
      else:
        print('to low')
        z=float(input('enter a number from 1 to 9.:'))
        count=count+1
    print ('nice game')
    return count
    

y = input('Hit any key to Play Game. Enter exit to stop')
guesses=0
while y != 'exit':
  guesses=guesses+play_game()
  y = input('Hit any key to Play Game. Enter exit to stop')
print('Thanks for playing. You took',guesses,'guesses')



    
    
