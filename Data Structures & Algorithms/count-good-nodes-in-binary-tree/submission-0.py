# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    good = 0
    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, root.val)
        return self.good
        
    def dfs(self, root: TreeNode, current_max: int):    
        if root is None:
            return 0
        
        new_max = max(current_max, root.val)

        if root.val >= current_max:
            self.good += 1

        self.dfs(root.left, new_max)
        self.dfs(root.right, new_max)
        
        return self.good
        