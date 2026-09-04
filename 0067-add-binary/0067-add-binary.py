class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i=len(a)-1
        j=len(b)-1
        carry=0
        res=""
        while i>=0 or j>=0 or carry:
            digit_a=int(a[i]) if i>=0 else 0
            digit_b=int(b[j]) if j>=0 else 0
            tot=digit_a+digit_b+carry
            res=str(tot%2)+res
            carry=tot//2
            i-=1
            j-=1
        return res