scores=float(input('What is your score?'))
def letterGrade(score):
    if score <= 59:
        letter = 'F'
    elif score <= 69:
        letter = 'D'
    elif score <= 79:
        letter = 'C'
    elif score <= 89:
        letter = 'B'
    else:
        letter = 'A'
    print('Your grade is '+letter+'.')

letterGrade(scores)
