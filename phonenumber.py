phone=input('Enter a mobile number:')
numbers={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
nums=[]
for x in range(0,len(phone)):
    if phone[x] in numbers:
        del[numbers[str(phone[x])]]
print(numbers)
