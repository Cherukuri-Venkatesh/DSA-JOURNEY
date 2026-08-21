class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s=set()
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            s.add(nums[i])

            if len(s)>k:
                s.remove(nums[i-k])
        return False
        