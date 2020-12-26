with open('nums 1.txt', 'r') as open_file:
    x = open_file.read()
with open('nums 2.txt', 'r') as open_file:
    y = open_file.read()
z=[]
for num in x and y:
    if num in x and y:
        z.append(num)
print(z)
