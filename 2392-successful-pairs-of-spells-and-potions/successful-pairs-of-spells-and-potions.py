from typing import List
from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        result = []
        
        for spell in spells:
            # Minimum potion needed: ceil(success / spell)
            min_potion = (success + spell - 1) // spell
            # First index where potion >= min_potion
            idx = bisect_left(potions, min_potion)
            result.append(n - idx)
        
        return result
