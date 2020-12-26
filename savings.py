def calc():
    bal=float(input('What is your initial balance?'))
    perc=float(input('What is your annual percentage for interest as a decimal?'))
    tar=float(input('What is your target?'))
    print(bal)
    while not bal >=tar:
        bal=(1+perc)*bal
        print(bal)
        
        
        

    
        

calc()
