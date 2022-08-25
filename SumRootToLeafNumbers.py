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
        stack = [root]
        res = 0
        while stack:
            node = stack.pop()
            if node.left:
                node.left.val += node.val*10
                stack.append(node.left)
            if node.right:
                node.right.val += node.val*10
                stack.append(node.right)
            elif not node.left:
                res += node.val
        return res
              