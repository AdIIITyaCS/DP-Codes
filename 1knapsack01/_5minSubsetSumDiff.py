from functools import reduce
def minSubsetSumDiff(arr):
  n=len(arr)
  sum = reduce(lambda x, y: x + y, arr)
  def subsetSum(arr,sum,n):
    a=[]
    mat=[[False for _ in range(sum+1)] for _ in range(n+1)]
    for i in range(n+1):
      mat[i][0]=True
    for i in range(1,n+1):
      for j in range(1,sum+1):
        if arr[i-1]<=j:
          mat[i][j]=mat[i-1][j-arr[i-1]] or mat[i-1][j]
        else:
          mat[i][j]=mat[i-1][j]
    sum=sum//2
    for i in range(sum+1):
      if mat[n][i]==True:
        a.append(i)
    return a
  a=subsetSum(arr,sum,n)
  mn=float('inf')
  for i in range(len(a)):
    mn=min(mn,sum-a[i]*2)
  return mn
# arr=[1,2,7]
arr=[1, 6, 11, 5]
print(minSubsetSumDiff(arr))
