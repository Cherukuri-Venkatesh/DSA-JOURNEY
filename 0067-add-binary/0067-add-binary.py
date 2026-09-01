class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_d=int(a,2)
        b_d=int(b,2)
        tot=a_d+b_d
        if tot==0:
            return '0'
        binary_str=""
        while tot>0:
            bit=tot&1
            binary_str=str(bit)+binary_str
            tot=tot>>1
        return binary_str
        