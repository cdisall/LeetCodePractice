# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        self.max = 0
        self.diameter(root)
        return self.max

    def diameter(self, node):
        if node:
            l = self.diameter(node.left)
            r = self.diameter(node.right)
            if l + r > self.max:
                self.max = l + r
            return max(l,r) + 1
        return 0