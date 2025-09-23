# def coinChange(coin,sum):
def coinChange(wt,W,n):
  t=[[float('-inf')-1 for _ in range(W+1)] for _ in range(n+1)]
  for i in range(n+1):
    t[i][0]=0
  # print(t)
  for j in range(1, W + 1):
    if j % wt[0] == 0:
      t[1][j] = j // wt[0]
    else:
      t[1][j] = float('inf')-1
  for i in range(2,n+1):
    for j in range(1,W+1):
      if wt[i-1]<=j:
        t[i][j]=min(1+ t[i][j-wt[i-1]], t[i-1][j])
      else:
        t[i][j]=t[i-1][j]
  print(t)
  return t[n][W] if t[n][W] != float('inf') else -1  # -1 means not possible
	    
# W = 3
# val = [1, 2, 3]
coin = [1, 2,3]
n = len(coin)
s=5
s1=1
c1=[2,5 ,7 ,12 ,15 ,16]
n1=len(c1)
# print(coinChange(coin,s,n))
print(coinChange(c1,s1,n1))
