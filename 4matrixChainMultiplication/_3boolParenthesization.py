# # Recursion
# def boolParenthesization(s,i,j,isTrue):
#     if i>j:
#         return 0
#     if i==j:
#         if isTrue=='T':
#             return 1 if s[i]=='T' else 0
#         else:
#             return 1 if s[i]=='F' else 0
#     ans=0
#     for k in range(i+1,j,2):
#         lT=boolParenthesization(s,i,k-1,'T')
#         lF=boolParenthesization(s,i,k-1,'F')
#         rT=boolParenthesization(s,k+1,j,'T')
#         rF=boolParenthesization(s,k+1,j,'F')
#         if s[k]=='&':
#             if (isTrue=='T'):
#                 ans+=lT*rT
#             else:
#                 ans+= lT*rF + lF*rF + lF*rT
#         elif s[k]=='|':
#             if (isTrue=='T'):
#                 ans+=lT*rT +  lT*rF + lF*rT   
#             else:
#                 ans+= lF*rF
#         elif s[k]=='^':
#             if (isTrue=='T'):

#                 ans+= lT*rF + lF*rT 
                
#             else:
#                 ans+=lT*rT + lF*rF
#         # print(ans)
#     return ans
# s = "T|T&F^T"
# # Output: 4
# n=len(s)
# print(boolParenthesization(s,0,n-1,'T'))

# Memoisation
def count(s):
    n = len(s)
    dp = {}

    def boolParenthesization(s, i, j, isTrue):
        key = (i, j, isTrue)
        if i > j:
            return 0
        if key in dp:
            return dp[key]

        if i == j:
            if isTrue == 'T':
                dp[key] = 1 if s[i] == 'T' else 0
            else:
                dp[key] = 1 if s[i] == 'F' else 0
            return dp[key]

        ans = 0
        for k in range(i + 1, j, 2):
            lT = boolParenthesization(s, i, k - 1, 'T')
            lF = boolParenthesization(s, i, k - 1, 'F')
            rT = boolParenthesization(s, k + 1, j, 'T')
            rF = boolParenthesization(s, k + 1, j, 'F')

            if s[k] == '&':
                if isTrue == 'T':
                    ans += lT * rT
                else:
                    ans += lT * rF + lF * rF + lF * rT
            elif s[k] == '|':
                if isTrue == 'T':
                    ans += lT * rT + lT * rF + lF * rT
                else:
                    ans += lF * rF
            elif s[k] == '^':
                if isTrue == 'T':
                    ans += lT * rF + lF * rT
                else:
                    ans += lT * rT + lF * rF

        dp[key] = ans
        return ans

    return boolParenthesization(s, 0, n - 1, 'T')


s = "T|T&F^T"
print(count(s))  # Output: 4
