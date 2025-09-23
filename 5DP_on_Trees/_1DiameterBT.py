class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
    def traverse(self, root):
        if root is None:
            return
        print(root.data, end=" ")
        self.traverse(root.left)
        self.traverse(root.right)
      
        
class Solution:
    def diameter(self, root):
        self.res = float('-inf')  # store maximum diameter

        def height(node):
            if node is None:
                return 0

            # compute height of left and right subtrees
            l = height(node.left)
            r = height(node.right)

            # update diameter (longest path through this node)
            self.res = max(self.res, 1 + l + r)

            # return height of tree rooted at this node
            return 1 + max(l, r)

        height(root)
        return self.res +1


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    # print(root.diameter(root))
    # Preorder traversal
    print("Preorder Traversal:", end=" ")
    root.traverse(root)
    print()

    # Diameter of tree
    sol = Solution()
    print("Diameter of tree:", sol.diameter(root))