# Similar as unbounded KS
# wt[]-->coin[]
# W-->sum
def coinChange(wt,W,n):
  t=[[0 for _ in range(W+1)] for _ in range(n+1)]
  for i in range(n+1):
    t[i][0]=1
  print(t)
  for i in range(1,n+1):
    for j in range(W+1):
      if wt[i-1]<=j:
        t[i][j]=t[i][j-wt[i-1]]+t[i-1][j]
      else:
        t[i][j]=t[i-1][j]
  print(t)
  return t[n][W]
# W = 3
# val = [1, 2, 3]
coin = [1, 2,3]
n = len(coin)
s=5
print(coinChange(coin,s,n))