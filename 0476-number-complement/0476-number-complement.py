class Solution:
    def findComplement(self, num: int) -> int:
        ans=0
        p=0
        while num>0:
            bit=num&1
            if bit==0:
                ans=ans | (1<<p)
            num=num>>1
            p+=1
        return ans
        