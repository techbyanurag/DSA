# Template code provided by LeetCode
class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        
        while left <= right:
            mid = left + (right - left) // 2
            guess_result = guess(mid)
            
            if guess_result == 0:
                return mid
            elif guess_result == 1:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
