
# Using Top down approach
def unboundedKS(wt,val,W,n):
    matrix = [[0 for _ in range(W+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, W+1):
            if wt[i-1] <= j:
                matrix[i][j] = max(val[i-1] + matrix[i][j - wt[i-1]], matrix[i-1][j])
            else:
                matrix[i][j] = matrix[i-1][j]
    return matrix[n][W]

val1 = [1, 1]
wt1 = [2, 1]
W1 = 3
n1=len(val1)
# print(unboundedKS(wt,val,W,n))
print(unboundedKS(wt1,val1,W1,n1))
