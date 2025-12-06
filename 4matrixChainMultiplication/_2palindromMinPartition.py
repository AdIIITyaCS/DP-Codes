# this code is of n^3 complexity we have to reduce the complexity by optimising the palindrome code and avoid multiple times function call
def palindromeMinPartioning(s):
    def isPalindrome(s,i,j):
        if i>=j:
            return True
        while (i<j):
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True

    n=len(s)
    mat=[[-1 for _ in range(n+1)] for _ in range(n+1)]
    
    def MCM(i,j):
        if i>=j or isPalindrome(s,i,j):
            return 0
        
        if mat[i][j]!=-1:
            return mat[i][j]

        mn=float('inf')
        for k in range(i,j):
            if mat[i][k]!=-1:
                left=mat[i][k]
            else:
                left=MCM(i,k)
                mat[i][k]=left
            if mat[k+1][j]!=-1:
                right=mat[k+1][j]
            else:
                right=MCM(k+1,j)
                mat[k+1][j]=right
            temp=left+right+1
            mn=min(mn,temp)
        mat[i][j]=mn
        return mn
    return MCM(0,n-1)
# s="ababbbabbababa"
s="nitin"
# n=len(s)
print(palindromeMinPartioning(s))

# s="nikjs"
# n=len(s)
# # print(s[::-1])
# print(s[0:n][::-1])