# by finding whole lcs string
# def sequencePatternMatching(a,b):
#     m=len(a)
#     n=len(b)
#     def LCSprint(a,b):
#         m=len(a)
#         n=len(b)
#         mat=[[-1 for _ in range(n+1)] for _ in range(m+1)]
#         for i in range(m+1):
#             for j in range(n+1):
#                 if i==0 or j==0:
#                     mat[i][j]=0
#         for i in range(m+1):
#             for j in range(n+1):
#                 if a[i-1]==b[j-1]:
#                     mat[i][j]=mat[i-1][j-1]+1
#                 else:
#                     mat[i][j]=max(mat[i-1][j],mat[i][j-1])
#         # mat[m][n]
#         ans=""
#         while i>0 and j>0:
#             if a[i-1]==b[j-1]:
#                 ans+=b[j-1]
#                 i-=1
#                 j-=1
#             else:
#                 if mat[i-1][j]>mat[i][j-1]:
#                     i-=1
#                 else:
#                     j-=1
#         # print(ans[::-1])
#         return ans[::-1]
    
#     if m==0 and n>0 or m==0 and n==0:
#         return a
#     if m>0 and n==0:
#         return False
#     return LCSprint(a,b)==a
# a="axyz"
# b=""
# a1=""
# b1="ahbgdc"
# # print(LCSprint(a,b))
# print(sequencePatternMatching(a,b))
# # print(sequencePatternMatching(a1,b1))





# by finding only length 
def sequencePatternMatching(a,b):
    m=len(a)
    n=len(b)
    def LCS(a,b):
        m=len(a)
        n=len(b)
        mat=[[-1 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    mat[i][j]=0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if a[i-1]==b[j-1]:
                    mat[i][j]=mat[i-1][j-1]+1
                else:
                    mat[i][j]=max(mat[i-1][j],mat[i][j-1])
        # print(mat[m][n])
        return mat[m][n]
    x=LCS(a,b)
    print(x)
    if LCS(a,b)==m:
        return True
    else:
        return False

    # return LCS(a,b)==m 
# a="axyz"
# b=""
a1="abg"
b1="ahbgdc"
# print(LCSprint(a,b))
# print(sequencePatternMatching(a,b))
print(sequencePatternMatching(a1,b1))