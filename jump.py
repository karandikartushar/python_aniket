def jump(num):
    if num%2 == 0:
      return num//2
    else:
      return 3*num+1

a = int(input('Enter an input value :'))
x=jump(a)
print(x)
while x!=1:
    x=jump(x)
    print(x)
    



    
    
