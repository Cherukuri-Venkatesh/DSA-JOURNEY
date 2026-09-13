class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor=0
        for i in range(len(nums)):
            xor=xor^nums[i]

        right=(xor&xor-1)^xor
        b1,b2=0,0
        for i in range(len(nums)):
            if nums[i]&right:
                b1=b1^nums[i]
            else:
                b2=b2^nums[i]
        return [b1,b2]
        