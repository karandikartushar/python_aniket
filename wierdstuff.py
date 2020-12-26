a=0
while a==0:
    para=input('Enter a paragraph:')
    length={}
    counter={}
    paralist = para.split()
    for x in range(0,len(paralist)):
        if str(paralist[x]) not in counter:
            counter.update({paralist[x]:1})
        else:
            counter[paralist[x]]+=1
        length.update({str(paralist[x]):int(len(paralist[x]))})
    maximum=max([i for i in counter.values()])
    longest=max([i for i in length.values()])
    for key,value in counter.items():
        if value==maximum:
            print('The word which occurs the most is '+str(key))
    for key,value in length.items():
        if value==longest:
            print('The longest word is '+str(key))       
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
