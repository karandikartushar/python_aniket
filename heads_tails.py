import random

def flip():
    x=random.randrange(2)
    if x==0:
        print('heads')
    else:
        print('tails')

for x in range(1,11):
    flip()
