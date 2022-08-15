# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        return self.diameter(root)

    def height(self, node):
        if node:
            return max(self.height(node.left), self.height(node.right)) + 1
        return 0

    def diameter(self, node):
        if node:
            return max((self.height(node.left) + self.height(node.right)), self.diameter(node.right), self.diameter(node.left))
        return 0