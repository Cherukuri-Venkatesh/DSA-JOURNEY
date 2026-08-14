class Solution(object):
    def findMiddleIndex(self, nums):
        prefix=[0]*len(nums)
        prefix[0]=nums[0]
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]+nums[i]
        
        total=prefix[-1]
        for i in range(len(nums)):
            if i==0:
                left=0
            else:
                left=prefix[i-1]
            right=total-left-nums[i]
            if left==right:
                return i
                break
        return -1

        