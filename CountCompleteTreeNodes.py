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
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        if lheight == rheight:
            return (pow(2, lheight)) + self.countNodes(root.right)
        else:
            return (pow(2, rheight)) + self.countNodes(root.left)
        
   
    def height(self, node):
        if not node:
            return 0
        return 1 + self.height(node.left)