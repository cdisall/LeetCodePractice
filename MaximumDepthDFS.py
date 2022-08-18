# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root, 0)
    def depth(self, node, max_depth):
        if node:
            return max(self.depth(node.left, max_depth), self.depth(node.right, max_depth)) + 1
        return max_depth