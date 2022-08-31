# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            if not subRoot:
                return True
            return False
        if self.same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def same(self, m, n):
        if None in [m,n]:
            if not m and not n:
                return True
            return False
        if m.val != n.val:
            return False
        return self.same(m.left, n.left) and self.same(m.right, n.right)