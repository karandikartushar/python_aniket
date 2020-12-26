x = open("test_file.txt","r+")
op=x.read(1)
a=x.read()
a=list(a)
b=0
if op=='A':
    for i in range(0,len(a)):
        if a[i].isnumeric()==True:
            b+=int(a[i])
if op=='S':
    for i in range(0,len(a)):
        if a[i].isnumeric()==True:
            if i==0:
                b+=int(a[i])
            else:
                b-=int(a[i])
if op=='M':
    b=1
    for i in range(0,len(a)):
        if a[i].isnumeric()==True:
            b*=int(a[i])
if op=='D':
    if a[0].isnumeric()==True and a[1].isnumeric()==True:
        b=int(a[0])/int(a[1])
b=str(b)
x.write(b)
x.close()
