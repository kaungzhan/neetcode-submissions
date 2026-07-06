# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count = 0
    answer = None 
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.dfs(root, k)
        return self.answer
    def dfs(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        self.dfs(root.left, k)
        self.count += 1
        if k == self.count:
            self.answer = root.val 
            return
        self.dfs(root.right, k)