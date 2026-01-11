from collections import defaultdict
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_count = defaultdict(int)
        # Count row tuples
        for i in range(n):
            row_count[tuple(grid[i])] += 1
        
        # Transpose and count matches
        ans = 0
        for j in range(n):
            col = tuple(grid[k][j] for k in range(n))
            ans += row_count[col]
        
        return ans
