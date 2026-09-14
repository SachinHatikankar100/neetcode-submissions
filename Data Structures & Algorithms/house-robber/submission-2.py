class Solution:
    def rob(self, nums: List[int]) -> int:
        #Recursion Approach
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     return max(dfs(i+1), nums[i]+dfs(i+2))
        # return dfs(0)

        #Dynamic Approach Top Down
        # memo = [-1] * len(nums)
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     if memo[i] != -1:
        #         return memo[i]
        #     memo[i] = max(dfs(i+1), nums[i]+dfs(i+2))
        #     return memo[i]
        
        # return dfs(0)
        #Dynamic Approach Bottom up

        #Dynamic Approach Space Optimized
        rob1, rob2 = 0, 0
        for num in nums:
            temp = max(num+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

        