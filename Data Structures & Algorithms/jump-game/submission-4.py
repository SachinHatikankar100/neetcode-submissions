class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #Recursion Approach
        # def dfs(i):
        #     if i == len(nums)-1:
        #         return True
        #     end = min(len(nums)-1, i + nums[i])
        #     for j in range(i+1, end + 1):
        #         if dfs(j):
        #             return True
        #     return False
        # return dfs(0)

        #Dynamic Bottom up approach

        # n = len(nums)
        # dp = [False] * n
        # dp[-1] = True
        # for i in range(n-2, -1, -1):
        #     end = min(n, i + nums[i]+1)
        #     for j in range(i+1, end):
        #         if dp[j]:
        #             dp[i] = True
        #             break
        # return dp[0]


        #Dynamic Top Down approach
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(nums)-1:
                return True
            if nums[i] == 0:
                return False
            end = min(len(nums), i + nums[i]+1)
            for j in range(i+1, end):
                if dfs(j):
                    memo[i]=True
                    return True
            memo[i]=False
            return False
        return dfs(0)

        #Greedy Approach
        # goal = len(nums)-1
        # for i in range(len(nums)-2, -1, -1):
        #     if i + nums[i] >= goal:
        #         goal = i
        # return goal == 0

        