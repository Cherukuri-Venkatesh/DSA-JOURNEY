class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr=[0]*(2*n)
        for i in range(2*n):
            if i%2==0:
                arr[i]=nums[i//2]
            else :
                arr[i]=nums[n+(i//2)]
        return arr
        