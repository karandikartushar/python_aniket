x=input('Enter some numbers:')
x=list(x)
print(x)
while len(x)>2:
    print(x[2])
    del x[2]
    print(x)
