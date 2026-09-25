class Solution:
    def findMin(self, nums: list[int]) -> int:
        nums.sort()
        l=0
        h=len(nums)-1
        while l<h:
            m=(l+h)//2
            if nums[m]>nums[h]:
                l=m+1
            if nums[m]<=nums[h]:
                h=m
        return nums[l]