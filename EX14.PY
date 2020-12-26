def main(nums):
    a=[]
    for num in nums:
        if num not in a:
            a.append(num)
    return a


x=main(input('Enter a list'))
print(x)
            
