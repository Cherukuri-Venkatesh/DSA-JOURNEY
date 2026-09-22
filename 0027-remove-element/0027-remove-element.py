class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        c=0
        for num in nums:
            if num!=val:
                nums[c]=num
                c+=1
        return c
        