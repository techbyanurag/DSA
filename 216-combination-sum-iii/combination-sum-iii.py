from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, path, remaining):
            if remaining == 0 and len(path) == k:
                result.append(path[:])
                return
            if remaining < 0 or len(path) == k:
                return
                
            for i in range(start, 10):
                path.append(i)
                backtrack(i + 1, path, remaining - i)
                path.pop()
        
        result = []
        backtrack(1, [], n)
        return result
