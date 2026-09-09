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

        n = len(nums)
        dp = [False] * n
        dp[-1] = True
        for i in range(n-2, -1, -1):
            end = min(n, i + nums[i]+1)
            for j in range(i+1, end):
                if dp[j]:
                    dp[i] = True
                    break
        return dp[0]


        