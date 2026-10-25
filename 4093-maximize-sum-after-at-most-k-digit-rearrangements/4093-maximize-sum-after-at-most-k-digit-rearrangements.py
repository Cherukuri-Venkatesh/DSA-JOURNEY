class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        arr=nums[:]
        extra_val=[]

        for num in arr:
            max_num=int(''.join(sorted(str(num),reverse=True)))
            extra_val.append(max_num-num)
        extra_val.sort(reverse=True)
        total=sum(arr)
        for i in range(k):
            total+=extra_val[i]
        return total
        