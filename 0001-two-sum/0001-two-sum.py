class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in seen:
                return [seen[complement],i]
                break
            seen[nums[i]]=i
        