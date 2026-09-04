class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=""
        for i in range(len(digits)):
            a+=str(digits[i])
        a=int(a)
        a=a+1
        a=str(a)
        ans=[]
        for ch in a:
            ans.append(int(ch))
        return ans




        