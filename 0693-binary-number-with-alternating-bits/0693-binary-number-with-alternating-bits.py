class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        while n>0:
            a=n&1
            b=(n>>1)&1
            if a==b:
                return False
                break
            n=n>>1
        return True

        