x = open("altcap1.txt","r+")
e=x.read()
e=str(e)
e=list(e)
z=0
a=2
y=[]
for i in range(0,len(e)):
    if e[i].isalpha()==False:
        a+=1
        if a%2==1:
            z+=1
        else:
            z=0
        y.append(e[i])
    else: 
        if i%2==z:
            y.append(e[i].upper())
        else:
            y.append(e[i].lower())
    
    
y = ''.join(map(str, y))
x.write("\n")
x.write(y)
x.close()




  
