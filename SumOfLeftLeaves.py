# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0
        s = [(root, False)]
        while s:
            node, left = s.pop()
            if left and not node.left and not node.right:
                res += node.val
            if node.left:
                s.append((node.left, True))
            if node.right:
                s.append((node.right, False))
        return res
