x=int(input('Enter a number:'))
nums=range(1,x+1)
for num in nums:
    if x%num==0:
        print(num)
