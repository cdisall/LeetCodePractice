# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.flat(root, None)
    
    def flat(self,node, tail): 
        if not node:
            return tail
        node.right = self.flat(node.left, self.flat(node.right, tail))
        node.left = None
        return node