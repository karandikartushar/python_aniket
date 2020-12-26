import sys 
max_num=int(input('Enter the maximum number:'))
num_sum=int(input('Enter the sum ofthe numbers:'))
nums=[]
if num_sum==0 and max_num==0:
    sys.exit()
for x in range(1,max_num+1):
    for i in range(1,max_num+1):
        if x+i==num_sum:
            z=str(x)+str(i)
            z=int(z)
            x=int(x)
            i=int(i)
            nums.append(z)
print(nums)
        
