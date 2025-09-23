def printShortestCommonSupersequence(a,b):
  m=len(a)
  n=len(b)
  mat=[[-1 for _ in range(n+1)] for _ in range(m+1)]
  ans=""
  for i in range(m+1):
    for j in range(n+1):
      if i==0 or j==0:
        mat[i][j]=0        
  for i in range(1,m+1):
    for j in range(1,n+1):
      if a[i-1]==b[j-1]:
        mat[i][j]=1+mat[i-1][j-1]
      else:
        mat[i][j]=max(mat[i-1][j],mat[i][j-1])

  while i>0 or j>0:
    if a[i-1]==b[j-1]:
      ans+=a[i-1]
      i-=1
      j-=1
    else:
      if mat[i][j-1]>mat[i-1][j]:
        ans+=b[j-1]
        j-=1
      else:
        ans+=a[i-1]
        i-=1
  while i>0:
    ans+=a[i-1]
    i-=1
  while j>0:
    ans+=b[j-1]
    j-=1
  return ans[::-1]
X="acbcf"
Y="abcdaf"
print(printShortestCommonSupersequence(X,Y))
