# this question is similar as deletion in string to make it palindrome 
def minInsertionforPalindrome(a):
    m=len(a)
    n=m
    def LCS(a,b):
        mat=[[-1 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    mat[i][j]=0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if a[i-1]==b[j-1]:
                    mat[i][j]=1+ mat[i-1][j-1]
                else:
                    mat[i][j]=max(mat[i-1][j],mat[i][j-1])
        return mat[m][n]
    return m-LCS(a,a[::-1])
# a="aebcbda"
a="abcd"
print(minInsertionforPalindrome(a))