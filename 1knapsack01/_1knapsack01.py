#Recursion 
def knapsack(W, val, wt,n):
  if W==0 or n==0:
    return 0
  if wt[n-1]<=W:
    return max(val[n-1] + knapsack(W-wt[n-1],val,wt,n-1) , knapsack(W,val,wt,n-1))
  elif wt[n-1]>W:
    return knapsack(W,val,wt,n-1)
W = 3
val = [1, 2, 3]
wt = [4, 5, 1]
n=len(val)
print(knapsack(W,val,wt,n))
print("============")



# # # Using DP (Memoization)
# # def knapsack(W, val, wt,n):
# #   rows = n+1
# #   cols = W+1
# #   matrix = [[-1 for _ in range(cols)] for _ in range(rows)]
# #   if W==0 or n==0:
# #     return 0
# #   if matrix[n][W]!=-1:
# #     return matrix[n][W]
# #   if wt[n-1]<=W:
# #     matrix[n][W]=max(val[n-1] + knapsack(W-wt[n-1],val,wt,n-1) , knapsack(W,val,wt,n-1))
# #     return matrix[n][W]
# #   elif wt[n-1]>W:
# #     return knapsack(W,val,wt,n-1)
# # W = 3
# # val = [1, 2, 3]
# # wt = [4, 5, 6]
# # n=len(val)
# # print(knapsack(W,val,wt,n))




# # Using DP (Memoization)
# def knapsack(W, val, wt):
#     n = len(val)
#     matrix = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]

#     # Define an inner recursive function to use the matrix
#     def solve(W, n):
#         if W == 0 or n == 0:
#             return 0
#         if matrix[n][W] != -1:
#             return matrix[n][W]
#         if wt[n - 1] <= W:
#             matrix[n][W] = max(val[n - 1] + solve(W - wt[n - 1], n - 1) , solve(W, n - 1))
#         else:
#             matrix[n][W] = solve(W, n - 1)
#         return matrix[n][W]

#     return solve(W, n)

# # Inputs
# W = 3
# val = [1, 2, 3]
# wt = [4, 5, 1]

# print(knapsack(W, val, wt))  


# # Using Top down approach
# def KS(wt,val,W,n):
#     matrix = [[0 for _ in range(W+1)] for _ in range(n+1)]
#     for i in range(1, n+1):
#         for j in range(1, W+1):
#             if wt[i-1] <= j:
#                 matrix[i][j] = max(val[i-1] + matrix[i-1][j - wt[i-1]], matrix[i-1][j])
#             else:
#                 matrix[i][j] = matrix[i-1][j]
#     return matrix[n][W]
# W = 3
# val = [1, 2, 3]
# wt = [4, 5, 1]
# n = len(val)
# print(KS(wt,val,W,n))