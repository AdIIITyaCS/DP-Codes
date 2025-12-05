# Recursion 
def MCM(arr,i,j):
    mn=float('inf')
    if i>=j:
        return 0
    for k in range(i,j):
        temp=MCM(arr,i,k)+MCM(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
        # temp=MCM(arr,i,k-1)+MCM(arr,k,j)+arr[i-1]*arr[k-1]*arr[j]
        mn=min(temp,mn)
    return mn
arr=[2, 1, 3, 4]
n=len(arr)
print(MCM(arr,1,n-1))

# # Memoisation
# def MCM(arr,i,j):
#     # n=len(arr)
#     mat=[[-1 for _ in range(n+1)] for _ in range(n+1)]
#     mn=float('inf')
#     if i>=j:
#         return 0
#     if mat[i][j]!=-1:
#         return mat[i][j]
#     for k in range(i,j):
#         temp=MCM(arr,i,k)+MCM(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
#         # temp=MCM(arr,i,k-1)+MCM(arr,k,j)+arr[i-1]*arr[k-1]*arr[j]
#         mn=min(temp,mn)
#     mat[i][j]=mn
#     print(mat)
#     return mn
# # arr=[2, 1, 3, 4]
# arr=[2,9,3]
# n=len(arr)
# print(MCM(arr,1,n-1))