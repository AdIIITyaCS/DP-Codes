# Same as knapsack
# wt[]--> length[]
# val[]--> price[]
# N=len(price)
# W--> N
# n--> N
# t[N+1][len((length)+1)]

# def rodcut(price):
#   N = len(price)
#   length = [i+1 for i in range(N)]  # implicit lengths [1, 2, ..., N]
#   t = [[0 for _ in range(N+1)] for _ in range(N+1)]
#   for i in range(1, N+1):
#       for j in range(1, N+1):
#         if length[i-1] <= j:
#           t[i][j] = max(price[i-1] + t[i][j - length[i-1]], t[i-1][j])
#         else:
#           t[i][j] = t[i-1][j]

#   return t[N][N]

# price= [1, 5, 8, 9, 10, 17, 17, 20]
# price1=[3, 5, 8, 9, 10, 17, 17, 20]
# # N=len(price)
# # =len(price)
# print(rodcut(price))
# print(rodcut(price1))

def cutRod(price):
  N = len(price)
  dp = [0] * (N+1)
  
  for i in range(N):
    for j in range(1, N+1):
      if i + 1 <= j:
        dp[j] = max(dp[j], price[i] + dp[j - (i + 1)])
  return dp[N]
price= [1, 5, 8, 9, 10, 17, 17, 20]
print(cutRod(price))