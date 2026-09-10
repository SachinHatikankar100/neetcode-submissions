class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Brute Force Approach
        # n, res = len(nums), nums[0]
        # for i in range(n):
        #     cur = 0
        #     for j in range(i, n):
        #         cur += nums[j] 
        #         res = max(res, cur)
        # return res

        #Recursion Approach
        # def dfs(i, flag):
        #     if i == len(nums)-1:
        #         return max(0,nums[i]) if flag else nums[i]
        #     if flag:
        #         return max(0, nums[i] + dfs(i+1, True))
        #     return max(dfs(i+1, False), nums[i]+dfs(i+1, True))
        # return dfs(0, False)

        #Dynamic programming space optimized Approach
        # dp = [*nums]
        # for i in range(1, len(nums)):
        #     dp[i] = max(nums[i], nums[i] + dp[i-1])
        # return max(dp)

        #Kadanes Approach
        # maxSub, curSum = nums[0],0
        # for num in nums:
        #     if curSum<0:
        #         curSum = 0
        #     curSum += num
        #     maxSub = max(maxSub, curSum)
        # return maxSub

        #Divide and Conquer Approach
        # def dfs(l,r):
        #     if l>r:
        #         return float("-inf")
        #     m = (l+r)>> 1
        #     leftSum = rightSum = curSum = 0
        #     for i in range(m-1,l-1,-1):
        #         curSum += nums[i]
        #         leftSum = max(leftSum, curSum)
            
        #     curSum = 0
        #     for i in range(m+1, r+1):
        #         curSum += nums[i]
        #         rightSum = max(rightSum, curSum)
            
        #     return (max(dfs(l,m-1), dfs(m+1, r), leftSum + nums[m]+ rightSum))
            
        # return dfs(0, len(nums)-1)

        #Dynamic Prorgamming Top Down Approach
        memo = [[None]*2 for _ in range(len(nums))]
        def dfs(i, flag):
            if i == len(nums)-1:
                return max(0, nums[i]) if flag else nums[i]
            if memo[i][flag] is not None:
                return memo[i][flag]
            if flag:
                memo[i][flag] =  max(0, nums[i]+dfs(i+1, True))
            else:
                memo[i][flag] =  max(dfs(i+1, False), nums[i]+dfs(i+1, True))

            return memo[i][flag]
        return dfs(0, False)
        #Dynamic Programming Bottom Up Approach



