class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        arr=[]
        c=0
        for i in range(len(nums)):
            if nums[i]==0:
                c+=1
            else:
                arr.append(nums[i])
        for i in range(c):
            arr.append(0)
        for i in range(len(nums)):
            nums[i]=arr[i]
        