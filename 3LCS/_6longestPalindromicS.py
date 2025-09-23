def longestPalindromicSubsequence(a):
  m=len(a)
  n=len(a)
  def LCS(a,b):
    mat=[[-1 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
      for j in range(n+1):
        if i==0 or j==0:
          mat[i][j]=0
    for i in range(m+1):
      for j in range(n+1):
        if a[i-1]==b[j-1]:
          mat[i][j]=1+ mat[i-1][j-1]
        else:
          mat[i][j]=max(mat[i-1][j],mat[i][j-1])
    return mat[m][n]
  return LCS(a,a[::-1])
a="agbcba"
print(longestPalindromicSubsequence(a))

