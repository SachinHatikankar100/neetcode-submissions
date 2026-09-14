class Solution:
    def rob(self, nums: List[int]) -> int:
        #Recursion Approach
        # if len(nums)==1:
        #     return 0
        # def dfs(i, flag):
        #     if i >= len(nums) or (flag and len(nums)-1):
        #         return 0
        #     return max(dfs(i+1, flag), nums[i]+dfs(i+2, flag or i==0))
        
        # return max(dfs(0,True), dfs(1, False))
        #Dynamic Top down approach


        #Dynamic Bottom up approach
        #Dynamic Space optimized approach
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    def helper(self, nums):
        rob1, rob2 = 0, 0
        for num in nums:
            newRob = max(rob1+num, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2
