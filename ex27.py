matrix=[[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
n=int(input('Player 1-Enter the row you want to place your piece in:'))
r=int(input('Player 1-Enter the column you want to place your piece in:'))
if n==1 or 2 or 3 or 4 and r== 1 or 2 or 3 or 4:
    matrix[n-1][r-1]='x'
print(matrix)
for p in range(1,5):
    q=int(input('Player 2-Enter the row you want to place your piece in:'))
    s=int(input('Player 2-Enter the column you want to place your piece in:'))
    if q==1 or 2 or 3 or 4 and r== 1 or 2 or 3 or 4:
        matrix[q-1][s-1]='o'
    print(matrix)
    n=int(input('Player 1-Enter the row you want to place your piece in:'))
    r=int(input('Player 1-Enter the column you want to place your piece in:'))
    if n==range(1,4) and r==range(1,4):
        matrix[n-1][r-1]='x'
    print(matrix)
