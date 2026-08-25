class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s=set(nums)
        m=k
        while m in s:
            m+=k
        return m