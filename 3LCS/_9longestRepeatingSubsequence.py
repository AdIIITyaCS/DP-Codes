def longestRepeatingSubsequence(s):
  m=len(s)
  b=s
  n=len(b)
  # n=m
  mat=[[-1 for _ in range(n+1)] for _ in range(m+1)]
  for i in range(1+m):
    for j in range(1+n):
      if i==0 or j==0:
        mat[i][j]=0
  for i in range(1,m+1):
        
    for j in range(1,n+1):
      if s[i-1]==b[j-1] and i!=j:
        mat[i][j]=1+ mat[i-1][j-1]
      else:
        mat[i][j]=max(mat[i-1][j],mat[i][j-1])
  return mat[m][n]
a="axxzxy"
# a="aabebcdd"
print(longestRepeatingSubsequence(a))
