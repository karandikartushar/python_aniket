nums=input('Enter some numbers:')
numlist={}
for x in range(0,len(nums)):
    if nums[x] not in numlist:
        numlist.update({nums[x]:1})
    else:
        numlist[nums[x]]+=1
for x in range(0,len(numlist)):
    if numlist[nums[x]]>1:
        print('The number ',nums[x],' is repeating ',numlist[nums[x]],' times.')
