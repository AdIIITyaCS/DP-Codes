# this code is not working well on any format perfectly 


# # Recursion 
# def eggDropping(e,f):
#     mn=float('inf')
#     if f==0 or f==1 :
#         return f
#     if e==1:
#         return f
#     for k in range(1,f+1):
#         temp=1+ max(eggDropping(e-1,k-1),eggDropping(e,f-k))
#         mn=min(temp,mn) 
#     return mn
# # e=3
# # f=5
# e=2
# f=36
# print(eggDropping(e,f))





# Memoisation
def eggDropping(e, f, memo):
    mn = float('inf')
    if f == 0 or f == 1:
        memo[e][f]= f
        return f
    if e == 1:
        memo[e][f]= f
        return f
    # Already computed
    if memo[e][f] != -1:
        return memo[e][f]
    for k in range(1, f + 1):
        low = eggDropping(e - 1, k - 1, memo)
        high = eggDropping(e, f - k, memo)
        temp = 1 + max(low,high)
        mn = min(mn, temp)
    memo[e][f] = mn
    # print(memo)
    return mn 
e = 2
f = 36
memo=[[-1 for _ in range(f+1)] for _ in range(e+1)]
print(eggDropping(e, f,memo))  # Output: 8


# # Top Down
# def eggDropping(e, f, memo):
#     mn = float('inf')
#     mat=[[-1 for _ in range(f+1)] for _ in range(e+1)]
#     for i in range(e+1):
#         for j in range(f+1):


#     if f == 0 or f == 1:
#         return f
#     if e == 1:
#         return f
#     if memo[e][f] != -1:
#         return memo[e][f]
#     for k in range(1, f + 1):
#         if memo[e - 1] [k - 1]!=-1:
#             low=memo[e - 1][k - 1]
#         else:
#             low=eggDropping(e-1,k-1,memo)
#         if memo[e][f-k]!=-1:
#             high=memo[e][f-k]
#         else:
#             high=eggDropping(e,f-k,memo)
#         temp = 1 + max(low,high)
#         mn = min(mn, temp)

#     # Store result
#     memo[e][f] = mn
#     return mn

# e = 3
# f = 5
# memo=[[-1 for _ in range(f+1)] for _ in range(e+1)]
# print(eggDropping(e, f,memo))  # Output: 8
