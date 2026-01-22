class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minpro=10**5
        ans=0
        for i in prices:
            minpro=min(minpro,i)
            ans=max(ans,i-minpro)
        return ans