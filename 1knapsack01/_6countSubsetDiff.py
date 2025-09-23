from functools import reduce 
def countSubsetDiff(arr,diff):
  n=len(arr)
  sum = reduce(lambda x, y: x + y, arr)
  if (diff + sum)%2==1:
    return 0
  updatedSum=(diff + sum)//2

  def countSubsetSum(arr,sum,n):
    mat=[[0 for _ in range(sum+1)] for _ in range(n+1)]
    for i in range(n+1):
      mat[i][0]=1
    for i in range(1,n+1):
      for j in range(1+sum):
        if arr[i-1]<=j:
          mat[i][j]=mat[i-1][j]+mat[i-1][j-arr[i-1]]
        else:
          mat[i][j]=mat[i-1][j]
    return mat[n][sum]
  
  return countSubsetSum(arr,updatedSum,n)


arr=[1,1,2,3]
diff=1
arr1 = [5, 2, 6, 4]
diff1 = 3
arr2=[1, 3, 3, 2, 1]
diff2=5
print(countSubsetDiff(arr,diff))
print(countSubsetDiff(arr1,diff1))
print(countSubsetDiff(arr2,diff2))
