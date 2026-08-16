class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                return True
            else:
                d[nums[i]]=1
        return False
        #if any(value>1 for value in d.values()):
            #return True
        #else:
            #return False
        