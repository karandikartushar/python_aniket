numlist=[]
nums=int(input('Enter the number:'))
num=int(input('Enter the number of digits for your series:'))
def arithmetic():
    b=1
    for x in range(1,(num+1)):
        numlist.append(b)
        b+=nums
def geometric():
    b=1
    for x in range(1,(num+1)):
        numlist.append(b)
        b=b*nums
x=input("Say if you want a arithmetic or geometric series.'a' for arithmetic and 'g' for geometric:")
if x=='a':
    arithmetic()
elif x=='g':
    geometric()
else:
    print('Invalid input')
print(numlist)


    































