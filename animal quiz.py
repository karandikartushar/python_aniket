def check_guess(guess,answer):
    global score
    if guess==answer:
        print('correct answer')
        score=score+1
score=0
print('guess the animal')
guess1=input('which bear lives at the north pole?')
check_guess(guess1,'polar bear')
