class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def rec(i, bought):
            if i == len(prices):
                return 0
            if(i, bought) in dp:
                return dp[(i, bought)]
            ans = rec(i+1, bought)
            if bought:
                ans = max(ans, prices[i] + rec(i+1, False))
            else:
                ans = max(ans, -prices[i] + rec(i+1, True))
            dp[(i, bought)] = ans
            return ans
        return rec(0, False)