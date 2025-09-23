class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

    def traverse(self, root):
        if root is None:
            return
        print(root.data,end=" ")
        self.traverse(root.left)
        self.traverse(root.right)

# Example usage:
if __name__ == "__main__":
    # Create nodes
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
    # for i in range(1,7):


    # Traverse and print nodes
root.traverse(root)
