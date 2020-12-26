def row (count):
    print(' --- '*count)
def column (count):
    print('|    '*count+'|')
def matrix (count):
    for i in range (1, count):
        row (count)
        column (count)
    row(count)
count = int (input('Enter a number : '))
matrix (count)
