# similar as countsubsetdiff

from functools import reduce 
def targetSum(arr,target):
  n=len(arr)
  s = reduce(lambda x, y: x + y, arr)
  if (target + s)%2==1 or target+s<=0:
    return 0
  updatedSum=(target + s)//2

  def countSubsetSum(arr,s,n):
    mat=[[0 for _ in range(s+1)] for _ in range(n+1)]
    for i in range(n+1):
      mat[i][0]=1
    for i in range(1,n+1):
      for j in range(1+s):
        if arr[i-1]<=j:
          mat[i][j]=mat[i-1][j]+mat[i-1][j-arr[i-1]]
        else:
          mat[i][j]=mat[i-1][j]
    return mat[n][s]
  
  return countSubsetSum(arr,updatedSum,n)


arr = [1, 1, 1, 1, 1]
target = 3
arr1=[5]
target1=-15
print(targetSum(arr,target))
print(targetSum(arr1,target1))