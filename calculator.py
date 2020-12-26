def add():
    y=int(input('type an integer:'))
    z=int(input('type another integer:'))
    print(y,'+',z,'=',y+z)
def subtract():
    a=int(input('type an integer:'))
    b=int(input('type another integer:'))
    print(a,'-',b,'=',a-b)
def multiply():
    c=int(input('type an integer:'))
    d=int(input('type another integer:'))
    print(c,'x',d,'=',c*d)
def divide():
    e=int(input('type an integer:'))
    while e==0:
        e=int(input('type an integer:'))
    f=int(input('type another integer:'))
    while f==0:
        f=int(input('type another integer:'))
    print(e,'/',f,'=',e/f)
def find_the_remainder ():
    g=int(input('type an integer:'))
    while g==0:
        g=int(input('type an integer:'))
    h=int(input('type another integer:'))
    while h==0:
        h=int(input('type another integer:'))
    print('if ',g,' is divided by ',h,' the remainder is ',g%h)
def exit1():
        print('thank you for using my calculator.')

x=''
while(x !='exit'):
    x=input('what do you want to do?add,subtract,multiply,divde,find a remainder or exit:')
    if x=='add':
        add()
    elif x=='subtract':
        subtract()
    elif x=='multiply':
        multiply()
    elif x=='divide':
        divide()
    elif x=='find a remainder':
        find_the_remainder()
    elif x=='exit':
        exit1()


