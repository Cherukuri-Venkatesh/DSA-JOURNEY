class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        l=len(nums)
        c=0
        for i in range(0,l-1):
            if nums[i]>nums[i+1]:
                c+=1
                if c>1:
                    return False
                if i==0 or nums[i-1]<=nums[i+1]:
                    nums[i]=nums[i+1]
                else:
                    nums[i+1]=nums[i]
        return True    