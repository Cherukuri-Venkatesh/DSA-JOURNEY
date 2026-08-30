class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        c=0
        for x in set(nums):
            first=nums.index(x)
            last=len(nums)-1-nums[::-1].index(x)
            if nums[first:last+1].count(x)==last-first+1:
                c+=1
        return c
        