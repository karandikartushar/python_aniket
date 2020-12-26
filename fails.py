
A= input('Enter name of student:')
x= int (input('Enter math marks out of 100:'))
while x>=101:
    print('type correct marks')
    x= int (input('Enter math marks out of 100:'))
y= int (input('Enter science marks out of 100:'))
while y>=101:
    print('type correct marks')
    y= int (input('Enter math marks out of 100:'))
z= int (input('Enter english marks out of 100:'))
while z>=101:
    print('type correct marks')
    z= int (input('Enter math marks out of 100:'))
tm1=x+y+z
if tm1>=250 and tm1<=300:
    tm2='A+'
elif tm1>=200 and tm1 <=249:
    tm2='A'
elif tm1>=150 and tm1 <=199:
    tm2='B'
elif tm1>=100 and tm1 <=149:
    tm2='C'
elif tm1>=301:
    tm2='invalid marks'
else:
    tm2='Fail'

print (A,'got',tm1,'their grade is',tm2)



