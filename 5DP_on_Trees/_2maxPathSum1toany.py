# class Node:
#     def __init__(self,val):
#         self.data=val
#         self.left=None
#         self.right=None
# class Solution:
#     def diameter(self,root):
#         self.res=float('-inf')
#         def height(node):
#             if node==None:
#                 return 0
#             l=self.diameter(node.left)
#             r=self.diameter(node.right)
#             temp= max(max(l,r)+node.data,node.data)
#             ans=max(temp,node.data+l+r)
#             self.res=max(self.res,ans)
#             return temp
#         height(root)
#         return self.res+1
      
# if __name__ == "__main__":
#     root = Node(-17)
#     root.left = Node(11)
#     root.right = Node(4)
#     root.left.left = Node(20)
#     root.left.right = Node(-2)
#     root.right.left = Node(10)
# # Input: root[] = [-17, 11, 4, 20, -2, 10]
# # Output: 31
#     # Diameter of tree
#     sol = Solution()
#     print("Diameter of tree:", sol.diameter(root))



class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root):
        self.res = float('-inf')

        def solve(node):
            if node is None:
                return 0

            # get max path from left and right, ignore negatives
            l = max(0, solve(node.left))
            r = max(0, solve(node.right))

            # update global max with the best path through this node
            self.res = max(self.res, node.data + l + r)

            # return best single path including this node
            return node.data + max(l, r)

        solve(root)
        return self.res


if __name__ == "__main__":
    root = Node(-17)
    root.left = Node(11)
    root.right = Node(4)
    root.left.left = Node(20)
    root.left.right = Node(-2)
    root.right.left = Node(10)

    sol = Solution()
    print("Maximum Path Sum:", sol.maxPathSum(root))
