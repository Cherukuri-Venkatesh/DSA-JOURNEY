class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)):
            l=len(str(nums[i]))
            if l%2==0:
                c+=1
        return c

        