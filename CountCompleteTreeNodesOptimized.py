# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lheight = self.lheight(root)
        rheight = self.rheight(root)
        if lheight == rheight:
            return (1 << lheight) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
   
    def lheight(self, node):
        if not node:
            return 0
        return 1 + self.lheight(node.left)
    
    def rheight(self, node):
        if not node:
            return 0
        return 1 + self.rheight(node.right)