class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod , zero_count = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_count +=1
        
        if zero_count>1:
            return [0] * len(nums)
        
        ans = [0]*len(nums)
        for i, c in enumerate(nums):
            if zero_count: ans[i]=0 if c else prod
            else: ans[i] = prod//c
        return ans