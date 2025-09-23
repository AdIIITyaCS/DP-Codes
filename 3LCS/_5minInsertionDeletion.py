def minInsertionDeletion(a,b):
  m=len(a)
  n=len(b)
  def LCS(a,b):
    mat=[[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1,m+1):
      for j in range(1,n+1):
        if a[i-1]==b[j-1]:
          mat[i][j]=1+ mat[i-1][j-1]
        else:
          mat[i][j]= max(mat[i-1][j],mat[i][j-1])
    return mat[m][n]

  return [m-LCS(a,b),n-LCS(a,b)]
a="heap"
b="pea"
print(minInsertionDeletion(a,b))