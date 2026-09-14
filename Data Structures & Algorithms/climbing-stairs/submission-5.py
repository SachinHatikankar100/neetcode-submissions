class Solution:
    def climbStairs(self, n: int) -> int:
        #Recursion Approach
        # def dfs(i):
        #     if i >= n:
        #         return i==n
        #     return dfs(i+1) + dfs(i+2)
        # return dfs(0)

        #Dynamic Programming Top down approach
        # cache = [-1] * n
        # def dfs(i):
        #     if i >= n:
        #         return i ==n
        #     if cache[i] != -1:
        #         return cache[i]
        #     cache[i] = dfs(i+1) + dfs(i+2)
        #     return cache[i]
        # return dfs(0)

        #Dynamic Programming Bottom up approach

        #Dynamic Programming Space optimized approach
        one, two = 1, 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one


        #Maths Approach

        # sqrt5 = math.sqrt(5)
        # phi = (1 + sqrt5)/2
        # psi = (1 - sqrt5)/2
        # n += 1
        # return round((phi**n - psi**n)/sqrt5)
