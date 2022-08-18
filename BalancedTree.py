# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root:
            return self.balance(root) > -1
        return True
    def balance(self, node):
        if node:
            l = self.balance(node.left)
            r = self.balance(node.right)
            if l < 0 or r < 0 or abs(l - r) > 1:
                return -1
            return max(l, r) + 1
        return 0
        