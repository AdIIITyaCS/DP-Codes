def lcSubstring(X,Y,m,n):
  mat=[[-1 for _ in range(n+1)] for _ in range(m+1)]
  ans=0
  for i in range(m+1):
      mat[i][0]=0
  for j in range(n+1):
      mat[0][j] = 0

  for i in range(1,m+1):
    for j in range(1,n+1):
      if X[i-1]==Y[j-1]:
        mat[i][j]=1+ mat[i-1][j-1]
        ans=max(ans,mat[i][j])
      else:
        mat[i][j]=0 
  print(mat)
  return ans
# X="abcde"
# Y="abvcfe"
X="acbcf"
Y="abcdaf"
m=len(X)
n=len(Y)
print(lcSubstring(X,Y,m,n))