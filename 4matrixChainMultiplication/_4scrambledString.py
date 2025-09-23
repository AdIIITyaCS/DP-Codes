# # Recursion
# def scrambledString(a,b):
#     flag=False
#     n=len(a)
#     if len(a)!= len(b) or n<=0:
#         return False
#     if a==b:
#         return True
#     for i in range(1,n):
#         if (scrambledString(a[:i],b[-i:]) and scrambledString(a[i:],b[:-i])) or (scrambledString(a[:i],b[:i]) and scrambledString(a[i:],b[i:])):
#             flag=True
#             break
#     return flag


# a = "coder"
# b = "ocred"
# a1 = "great"
# b1 = "great"
# a2 = "great"
# b2 = "grdat"
# print(scrambledString(a, b))  # True
# print(scrambledString(a1, b1))  # True
# print(scrambledString(a2, b2))  # True




#Memoisation
def scrambledString(a,b):
    key=(a,b)
    if key in memo:
        return memo[key]


    flag=False
    n=len(a)

    if len(a)!= len(b) or n<=0:
        return False
    if a==b:
        return True
    for i in range(1,n):
        if (scrambledString(a[:i],b[-i:]) and scrambledString(a[i:],b[:-i])) or (scrambledString(a[:i],b[:i]) and scrambledString(a[i:],b[i:])):
            flag=True
            break
    
    # print(a[:],b[:])    
    memo[key]=flag
    # print(memo)
    return flag


a = "coder"
b = "ocred"
a1 = "great"
b1 = "great"
a2 = "great"
b2 = "grdat"
memo={}
print(scrambledString(a, b))  # True
print(scrambledString(a1, b1))  # True
print(scrambledString(a2, b2))  # True



