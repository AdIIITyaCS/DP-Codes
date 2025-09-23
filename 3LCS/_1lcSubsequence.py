# # #Recursion
# # def longestCommonSubsequence(X,Y,nx,ny):
# #   if nx==0 or ny==0:
# #     return 0
# #   # for 
# #   if X[nx-1]==Y[ny-1]:
# #     return 1+ longestCommonSubsequence(X,Y,nx-1,ny-1)
# #   else:
# #     return max(longestCommonSubsequence(X,Y,nx,ny-1),longestCommonSubsequence(X,Y,nx-1,ny))
# # X="abcde"
# # Y="abxde"
# # nx=len(X)
# # ny=len(Y)
# # print(longestCommonSubsequence(X,Y,nx,ny))
# # #Recursion

# #Memoisation
# def longestCommonSubsequence(X,Y,nx,ny):
#   mat=[[-1 for _ in range(nx+1)] for _ in range(ny+1)]
#   if nx==0 or ny==0:
#     return 0
#   if mat[ny][nx]!=-1:
#     return mat[ny][nx]
#   if X[nx-1]==Y[ny-1]:
#     mat[ny][nx]= 1+ longestCommonSubsequence(X,Y,nx-1,ny-1)
#     return mat[ny][nx]
#   else:
#     mat[ny][nx]= max(longestCommonSubsequence(X,Y,nx,ny-1),longestCommonSubsequence(X,Y,nx-1,ny))
#     return mat[ny][nx]
# X="abcd"
# Y="abxde"
# nx=len(X)
# ny=len(Y)
# print(longestCommonSubsequence(X,Y,nx,ny))


# Top-down (Memoization) approach
# def longestCommonSubsequence(X, Y, m, n):
#     mat = [[-1 for _ in range(n+1)] for _ in range(m+1)]

#     # Initialize base case
#     for i in range(m+1):
#         for j in range(n+1):
#             if i == 0 or j == 0:
#                 mat[i][j] = 0

#     # Fill DP table
#     for i in range(1, m+1):
#         for j in range(1, n+1):
#             if X[i-1] == Y[j-1]:
#                 mat[i][j] = 1 + mat[i-1][j-1]
#             else:
#                 mat[i][j] = max(mat[i][j-1], mat[i-1][j])
#     # print(mat)
#     return mat[m][n]

# # Example usage
# X=""
# Y="abcd"
# # X="agbcba"
# # Y="abcbga"
# m = len(X)
# n = len(Y)
# print(longestCommonSubsequence(X, Y, m, n))  # Output: 3




def longestCommonSubsequence(X, Y, m, n):
    mat = [[False for _ in range(n+1)] for _ in range(m+1)]

    # Initialize base case
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                mat[i][j] = True

    # Fill DP table
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                mat[i][j] = True
            else:
                mat[i][j] = mat[i][j-1] or mat[i-1][j]
    # print(mat)
    return mat[m][n]

# Example usage
X="e"
Y="abcd"
# X="abcdgh"
# Y="abedfhr"
m = len(X)
n = len(Y)
print(longestCommonSubsequence(X, Y, m, n))  # Output: 3
