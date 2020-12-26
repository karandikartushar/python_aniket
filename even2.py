def chooseEven(nums):
    even=([])
    for num in nums:
        if num % 2 == 0:
            even.append(num)
    return even

def uniqueList(nums):
    even=([])
    for num in nums:
        if num not in even:
            even.append(num)
    return even

print (uniqueList([2,4,5,7,9,8,8,2,5,9]))

