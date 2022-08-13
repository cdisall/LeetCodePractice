# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q):
        if None in [p,q]:
            return (p is None) == (q is None)
        stack = [(p,q)]
        while stack:
            x, y = stack.pop()
            if x.val != y.val:
                return False
            else:
                if x.left and y.left:
                    stack.append((x.left, y.left))
                elif (x.left is None) != (y.left is None):
                        return False
                if x.right and y.right:
                    stack.append((x.right, y.right))
                elif (x.right is None) != (y.right is None):
                        return False
        return True

