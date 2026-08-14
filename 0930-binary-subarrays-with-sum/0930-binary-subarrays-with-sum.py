class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        prefix=0
        count=0
        mp={0:1}
        for num in nums:
            prefix+=num
            
            t=prefix-goal
            if t in mp:
                count+=mp[t]
            mp[prefix]=mp.get(prefix,0)+1
        return count
        