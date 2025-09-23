def printlcSubsequence(X,Y):
  m=len(X)
  n=len(Y)
  mat = [[-1 for _ in range(n+1)] for _ in range(m+1)]  ##n+1 shows  

  # Initialize base case
  for i in range(m+1):  # 1st row , 2nd row, 3rd row.......m+1 row
      for j in range(n+1):   # 1st column , 2nd column, 3rd column.......m+1 column
          if i == 0 or j == 0:
              mat[i][j] = 0


  for i in range(m+1):
    for j in range(n+1):
      if X[i-1]==Y[j-1]:
        mat[i][j]=1+mat[i-1][j-1]
      else:
        mat[i][j]=max(mat[i-1][j],mat[i][j-1])
  ans=""  #for storing answer
  # print(i,j)
  while i>0 and j>0:
    if X[i-1]==Y[j-1]:
      ans=ans + X[i-1]
      i-=1
      j-=1
    else:
      if mat[i][j-1]>mat[i-1][j]:
        j-=1
      else:
        i-=1
  return ans[::-1]
# X=""
X="acbcf"
Y="abcdaf"
print(printlcSubsequence(X,Y))
