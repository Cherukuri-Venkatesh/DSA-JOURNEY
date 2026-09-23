class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        l=0
        h=len(nums)-1
        right=-1
        while l<=h:
            m=(l+h)//2
            if nums[m]<=target:
                right=m
                l=m+1
            else:
                h=m-1
        l=0
        h=len(nums)-1
        left=-1
        while l<=h:
            m=(l+h)//2
            if nums[m]>=target:
                left=m
                h=m-1
            else:
                l=m+1
        if right!=-1 and left!=-1 and nums[right]==target and nums[left]==target:
            return [left,right]
        else:
            return [-1,-1]
            

        