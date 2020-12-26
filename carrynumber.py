num1=input('Enter a number:')
num2=input('Enter a number:')
num3=int(0)
if num1>num2:
    num3+=int(num1)
elif num2>num1:
    num3+=int(num2)
else:
    num3+=num1
carry=0
plus=0
for x in range(1,len(str(num3))+1):
    b=(int(num1[-x]))+(int(num2[-x]))+plus
    if b>9:
        carry+=1
        b=str(b)
        plus=int(b[0])
        plus=int(plus)
print(carry)
