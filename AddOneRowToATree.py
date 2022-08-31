# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root: 
            return root
        if depth == 1:
            return TreeNode(val, root, None)
        stack = [(root, 1)]
        while stack:
            node, d = stack.pop()
            if not node:
                continue
            if d == depth - 1:
                ltmp = node.left
                rtmp = node.right
                node.left, node.right = TreeNode(val, ltmp, None), TreeNode(val, None, rtmp)
            stack.extend([(node.left, d + 1), (node.right, d + 1)])
        return root
