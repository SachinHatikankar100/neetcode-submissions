class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ## Brute Force
        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         return i
        # return -1

        #Binary Search approach
        # l, r = 0, len(nums)-1
        # while l<r:
        #     m = (l+r)//2
        #     if nums[m]>nums[r]:
        #         l = m+1
        #     else:
        #         r = m
        # pivot = l
        # def binary_search(left:int, right:int)-> int:
        #     while(left<=right):
        #         mid = (left+right)//2
        #         if nums[mid]==target:
        #             return mid
        #         elif nums[left]<target:
        #             left = mid + 1
        #         else:
        #             right = mid -1
        #     return -1
        # result = binary_search(0, pivot - 1)
        # if result != -1:
        #     return result
        
        # return binary_search(pivot, len(nums)-1)


        #Binary Search One pass
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            
            if nums[l]<=nums[mid]:
                if target>nums[mid] or target<nums[l]:
                    l = mid +1
                else:
                    r = mid -1
            else:
                if target<nums[mid] or target>nums[r]:
                    r = mid -1
                else:
                    l = mid +1
        return -1
        