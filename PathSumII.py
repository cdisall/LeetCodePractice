# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if not root: 
            return res
        stack = [(root, [root.val], targetSum - root.val)]
        while stack:
            node, l, summ = stack.pop()
            if not node.left and not node.right:
                if summ == 0:
                    res.append(l)
            if node.left:
                stack.append((node.left, l + [node.left.val], summ - node.left.val))
            if node.right:
                stack.append((node.right, l + [node.right.val], summ - node.right.val))
        return res
        