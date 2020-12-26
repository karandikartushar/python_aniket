import random
import string
for k in range(1,6):
    password=''
    for c in range(1,4):
        y=random.choice(string.ascii_lowercase)
        password=password+y
    for d in range(1,4):
        z=random.choice(string.ascii_uppercase)
        password=password+z
    a=random.choice(string.digits)
    password=password+a
    b=random.choice(string.punctuation)
    password=password+b
    print(password)


