# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root, targetSum) -> bool:
        return self.path(root, targetSum)
    
    def path(self, node, target):
        if node:
            if not (node.left or node.right):
                return (target == node.val)
            else:
                return (self.path(node.left, target - node.val) or self.path(node.right, target - node.val))
        return False