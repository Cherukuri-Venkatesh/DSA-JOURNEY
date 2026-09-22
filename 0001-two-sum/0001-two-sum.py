class Solution(object):
    def twoSum(self, nums, target):
        original=nums
        nums1=sorted(nums)
        p1=0
        p2=len(nums1)-1
        while p1<p2:
            sum1=nums1[p1]+nums1[p2]
            if sum1==target:
                ind=original.index(nums1[p1])
                if nums1[p1] == nums1[p2]:
                    ind2=original.index(nums1[p2], ind + 1)
                else:
                    ind2=original.index(nums1[p2])
                return [ind,ind2]
            elif sum1<target:
                p1+=1
            else:
                p2-=1
        return []
        
        