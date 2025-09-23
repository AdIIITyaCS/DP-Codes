# # Top down approach
# def isSubsetSum (arr, sum):
#     n=len(arr)
#     matrix = [[False for _ in range(sum+1)] for _ in range(n+1)]  
#     for i in range(n+1):
#       matrix[i][0] = True
#     for i in range(1, n + 1):
#         for j in range(1, sum + 1):
#             if arr[i - 1] <= j:
#                 matrix[i][j] = matrix[i - 1][j - arr[i - 1]] or matrix[i - 1][j]
#             else:
#                 matrix[i][j] = matrix[i - 1][j]

#     return matrix[n][sum]










def subsetSum(arr,sum,n):
    mat=[[False for _ in range(sum+1)] for _ in range(n+1)]
    for i in range(n+1):
        mat[i][0]=True
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if arr[i-1]<=j:
                mat[i][j]=mat[i-1][j-arr[i-1]] or mat[i-1][j]
            else:
                mat[i][j]=mat[i-1][j]
    return mat[n][sum]

arr = [1,5,5,11]
sum =11
arr1= [28, 4, 3, 27, 0, 24, 26]
sum1 = 24
n=len(arr)
n1=len(arr1)
print(subsetSum(arr,sum,n))
print(subsetSum(arr1,sum1,n1))

