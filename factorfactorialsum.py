num=int(input('Enter a number:'))
factors=[]
for x in range(1,num+1):
    if num%x==0:
        factors.append(x)
mul=1
plus=0
for x in range(0,len(factors)):
    for i in range(1,factors[x]+1):
        mul=mul*i
    plus+=mul
    mul-=mul
    mul+=1
print('The sum of the factorials of the factors of your number is '+str(plus)+'.')
