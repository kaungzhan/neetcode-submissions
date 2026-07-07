# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        l, r = 0, len(inorder) -1 
        self.pre_idx = 0
        self.position = {}
        for i in range(len(inorder)):
            self.position[inorder[i]] = i
        return self.build(preorder,l ,r)
    def build(self, preorder, left, right):
        if left > right:
            return None
        root_val = preorder[self.pre_idx]
        root = TreeNode(root_val)
        self.pre_idx += 1 
        mid = self.position[root_val]
        root.left = self.build(preorder, left, mid-1)
        root.right = self.build(preorder, mid+1, right)
        return root

