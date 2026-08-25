class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix=[0]*len(nums)
        prefix[0]=nums[0]
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]+nums[i]
        total=prefix[-1]
        for j in range(len(nums)):
            if j==0:
                left=0
            else:
                left=prefix[j-1]
            right=total-left-nums[j]
            if left==right:
                return j
                break
        return -1
