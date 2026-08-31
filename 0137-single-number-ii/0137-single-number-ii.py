class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        for i in range(32):
            c=0
            for num in nums:
                if (num>>i)&1:
                    c+=1
                
            if c%3!=0:
                ans=ans|(1<<i)
            if ans>=(1<<31):
                ans-=(1<<32)
        return ans

