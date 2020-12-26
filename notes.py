amount=int(input('Enter a number:'))
notes3=[500,200,100,50,20,10,5,1]
notes={500:0,200:0,100:0,50:0,20:0,10:0,5:0,1:0}
while amount!=0:
    for x in range(0,len(notes3)):
        if amount>=notes3[x]:
            amount-=notes3[x]
            notes[notes3[x]]+=1
            break
print(notes)
        
