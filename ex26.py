matrix = [[1, 2, 2],
    [1, 1, 2],
    [2, 2, 2]]
p1=[0,0,0]
p2=[0,0,0]
while 1!=2:
# checking the rows
  for i in range(0,3):
    for j in range(0,3):
        if matrix [i][j]==1:
            p1[i]+=1
        if matrix[i][j]==2:
            p2[i]+=1
  if p1[0]==3 or p1[1]==3 or p1[2]==3:
    print('player 1 wins - row')
    break
  if p2[0]==3 or p2[1]==3 or p2[2]==3:
    print('player 2 wins - row')
    break
  for k in range(0,3):
    p1[k]=0
    p2[k]=0
#checking the columns
  for j in range(0,3):
    for i in range(0,3):
            if matrix [i][j]==1:
                p1[i]+=1
            if matrix[i][j]==2:
                p2[i]+=1
  if p1[0]==3 or p1[1]==3 or p1[2]==3:
    print('player 1 wins - column')
    break
  if p2[0]==3 or p2[1]==3 or p2[2]==3:
    print('player 2 wins - column')
    break
  for k in range(0,3):
    p1[k]=0
    p2[k]=0
#checking the left to right diagonal
  for i in range(0,3):
    if matrix[i][i]==1:
        p1[i]+=1
    if matrix[i][i]==2:
        p2[i]+=1
  if p1[0]==1 and p1[1]==1 and p1[2]==1:
    print('player 1 wins - L to R')
    break
  if p2[0]==1 and p2[1]==1 and p2[2]==1:
    print('player 2 wins - L to R')
    break
  for k in range(0,3):
    p1[k]=0
    p2[k]=0
#checking the right to left diagonal
  for m in range(0,3):
    if matrix[m][-(m+1)]==1:
        p1[m]+=1
    if matrix[m][-(m+1)]==2:
        p2[m]+=1
  if p1[0]==1 and p1[1]==1 and p1[2]==1:
    print('player 1 wins - R to L')
    break
  if p2[0]==1 and p2[1]==1 and p2[2]==1:
    print('player 2 wins - R to L')
    break
    
