x=input('Enter a word:')
y=len(x)
if y % 2 == 0:
    no_compare = int(y/2+1)
else:
    no_compare = int((y-1)/2+1)
    
for z in range(1,no_compare):
    if x[z-1]==x[0-z]:
        result=True
    else:
        result=False
        break
if result==True:
    print('The word ',x,' is palindrome')
else:
    print('The word ',x,' is not palindrome')


if x == x[::-1]:
        print('The word ',x,' is palindrome')
else:
    print('The word ',x,' is not palindrome')
