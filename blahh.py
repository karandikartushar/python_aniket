def collatz(number):
    if number%2==0:
        x=number//2
    else:
        x=3*number+1
    return x
a=collatz(int(input('Enter a number:')))
while a!=1:
    print(a)
    a=collatz(a)
print(a)
