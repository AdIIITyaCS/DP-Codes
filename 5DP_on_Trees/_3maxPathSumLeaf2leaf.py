# This is not still working 










# class Node:
#     def __init__(self,val):
#         self.left=None
#         self.right=None
#         self.data=val


# class Solution:
#     def maxPathSum(self, root):
#         self.res = float('-inf')

#         def solve(node):
#             if node is None:
#                 return 0

#             # get max path from left and right, ignore negatives
#             l = solve(node.left)
#             r = solve(node.right)

#             # update global max with the best path through this node
#             self.res = max(self.res, node.data + l + r)

#             # return best single path including this node
#             return node.data + max(l, r)

#         solve(root)
#         return self.res


# if __name__ == "__main__":
#     root = Node(-17)
#     root.left = Node(11)
#     root.right = Node(4)
#     root.left.left = Node(20)
#     root.left.right = Node(-2)
#     root.right.left = Node(10)

#     sol = Solution()
#     print("Maximum Path Sum:", sol.maxPathSum(root))
