from collections import deque

class Solution:
    def maxLevelSum(self, root):
        q = deque([(root, 1)])
        max_sum, ans = float('-inf'), 1
        
        while q:
            level_sum, level_size = 0, len(q)
            for _ in range(level_size):
                node, lvl = q.popleft()
                level_sum += node.val
                if node.left: q.append((node.left, lvl+1))
                if node.right: q.append((node.right, lvl+1))
            
            if level_sum > max_sum:
                max_sum, ans = level_sum, lvl
        
        return ans
