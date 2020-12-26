def fib():
    x=int(input('enter the number of elements in fib series'))
    num1=1
    print(num1)
    num2=1
    print(num2)
    #num3=num1+num2
    #print(num3)
    for y in range(2,x):
        next1=num1+num2
        print(next1)
        num1=num2
        num2=next1
        

fib()
        
        
        
        
        
    
