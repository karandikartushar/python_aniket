def main(nums):
    x=int(input('Enter a number'))
    nums2=([])
    for num in nums:
        if num<x:
            nums2.append(num)
    print(nums2)

main([2,3,4,6,8,19,55])
        
        
