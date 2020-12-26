num=input('Enter a number:')
mul=1
plus=0
for x in range(0,len(num)):
    for i in range(1,int(num[x])+1):
        mul=mul*i
    plus+=mul
    mul-=mul
    mul+=1
print('The sum of the factorials of the digits of the number is '+str(plus)+'.')
