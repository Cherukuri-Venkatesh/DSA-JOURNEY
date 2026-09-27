class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        m={}
        ans=[]
        for i in range(len(nums)):
            if nums[i] in m:
                m[nums[i]]+=1
            else:
                m[nums[i]]=1
        while any(m.values()):
            val=[]
            for x in m:
                if m[x]>0:
                    val.append(x)
            val.sort()
            for x in val:
                ans.append(x)
                m[x]-=1
        return ans