def countSubsetSum(arr,sum):
  n=len(arr)
  mat=[[0 for _ in range(sum+1)] for _ in range(n+1)]
  for i in range(n+1):
    mat[i][0]=1
  for i in range(1,n+1):
    for j in range(0,sum+1):
      if arr[i-1]<=j:
        mat[i][j]=mat[i-1][j-arr[i-1]] + mat[i-1][j]
      else:
        mat[i][j]=mat[i-1][j]
  return mat[n][sum] 

arr=[2,3,5,6,8,10]
sum=10
arr1= [28, 4, 3, 27, 0, 24, 26]
sum1 = 24

print(countSubsetSum(arr, sum))
print(countSubsetSum(arr1, sum1))


# def countSubsetSum(arr, sum):
#     n = len(arr)
#     mat = [[0 for _ in range(sum + 1)] for _ in range(n + 1)]
#     for i in range(n + 1):
#         mat[i][0] = 1
#     for i in range(1, n + 1):
#         for j in range(0, sum + 1):
#             if arr[i - 1] == 0:
#                 mat[i][j] = mat[i - 1][j] * 2
#             elif arr[i - 1] <= j:
#                 mat[i][j] = mat[i - 1][j - arr[i - 1]] + mat[i - 1][j]
#             else:
#                 mat[i][j] = mat[i - 1][j]
#     return mat[n][sum]

# arr = [28, 4, 3, 27, 0, 24, 26]
# sum = 24

# # arr=[2,3,5,6,8,10]
# # sum=10

# print(countSubsetSum(arr, sum))