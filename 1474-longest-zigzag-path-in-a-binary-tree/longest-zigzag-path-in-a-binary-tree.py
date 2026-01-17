# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.max_length = 0
        
        def dfs(node: TreeNode, left_len: int, right_len: int) -> None:
            if not node:
                return
            self.max_length = max(self.max_length, left_len, right_len)
            dfs(node.left, right_len + 1, 0)
            dfs(node.right, 0, left_len + 1)
        
        dfs(root, 0, 0)
        return self.max_length
