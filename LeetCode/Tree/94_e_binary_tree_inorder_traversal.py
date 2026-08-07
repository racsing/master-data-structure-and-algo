class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class BinarySearchTree:
    def createNode(self, data):
        return Node(data)

    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        return node

    def inorderTraversal(self, root):
        if root is not None:
            self.inorderTraversal(root.left)
            print(root.data, end=",")
            self.inorderTraversal(root.right)


# Driver Code
values = [5, 2, 10, 7, 15, 12, 20, 30, 6, 8]
tree = BinarySearchTree()
root = None

# Create binary tree
for val in values:
    root = tree.insert(root, val)

# Printing INORDER TRAVERSAL
tree.inorderTraversal(root)
