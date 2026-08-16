class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=len(nums)
        total=l*(l+1)//2
        s=sum(nums)
        return total-s