class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        self.prefix=[0]*len(nums)
        self.prefix[0]=nums[0]
        for i in range(1,len(nums)):
            self.prefix[i]=self.prefix[i-1]+nums[i]
        for j in range(0,len(nums)):
            if j==0:
                if self.prefix[len(nums)-1]-self.prefix[0]==0:
                    return j 
                    break
            elif self.prefix[j-1]==self.prefix[len(nums)-1]-self.prefix[j]:
                return j
                break
        return -1


        
        