class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in dict:
                dict[nums[i]]=i
            else:
                return [dict[diff],i]
                
        