# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def path(node, p):
            if not node:
                return
            tmp = p + [str(node.val)]
            if not node.left and not node.right:
                res.append(tmp)
            if node.left:
                path(node.left, tmp)
            if node.right:
                path(node.right, tmp)
        path(root, [])
        return [ *map('->'.join, res) ]
            
