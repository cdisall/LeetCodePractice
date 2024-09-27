# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = []
        def add_level(level):
            s = 0
            new_level = []
            for i in level:
                s+=i.val
                if i.left!=None:
                    new_level.append(i.left)
                if i.right!=None:
                    new_level.append(i.right)
            sums.append(s)
            if len(new_level)>0:
                add_level(new_level)
        add_level([root])
        if len(sums)<k:
            return -1
        sums.sort(reverse=True)
        return sums[k-1]