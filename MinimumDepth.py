# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root)
    def depth(self, node):
        if not node:
            return 0
        if None in [node.left, node.right]:
            if node.left and not node.right:
                return 1 + self.depth(node.left)
            elif not node.left and node.right:
                return 1 + self.depth(node.right)
            else: 
                return 1
        return min(self.depth(node.left), self.depth(node.right)) + 1