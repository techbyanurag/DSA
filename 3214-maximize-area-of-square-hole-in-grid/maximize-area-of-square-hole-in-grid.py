class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: list[int], vBars: list[int]) -> int:
        def find_max_consecutive_gap(bars: list[int]) -> int:
            if not bars:
                return 1
            bars.sort()
            max_consecutive = current_consecutive = 1
            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    current_consecutive += 1
                    max_consecutive = max(max_consecutive, current_consecutive)
                else:
                    current_consecutive = 1
            return max_consecutive + 1
        
        max_h_gap = find_max_consecutive_gap(hBars)
        max_v_gap = find_max_consecutive_gap(vBars)
        side = min(max_h_gap, max_v_gap)
        return side * side
