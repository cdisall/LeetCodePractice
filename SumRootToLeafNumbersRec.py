# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.summ(root, "")
    
    def summ(self, node, num):
        if not node:
            return int(num)
        tmp = num + str(node.val)
        if None in [node.left, node.right]:
            if node.right:
                return self.summ(node.right, tmp)
            if node.left:
                return self.summ(node.left, tmp)
            else:
                return int(tmp)
        return self.summ(node.left, tmp) + self.summ(node.right, tmp)
        