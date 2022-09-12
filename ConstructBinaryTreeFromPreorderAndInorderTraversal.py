# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return
        # Get index of new root from preorder list
        rootVal = preorder.pop(0)
        i = inorder.index(rootVal)
        root = TreeNode(inorder[i])
        # Recurse with first half of inorder
        root.left = self.buildTree(preorder, inorder[:i])
        # Recurse with second half of inorder
        root.right = self.buildTree(preorder, inorder[i+1:])
        return root