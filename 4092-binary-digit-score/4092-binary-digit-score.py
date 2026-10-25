class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        s1,s2=0,0
        while a>0:
            if a&1==1:
                s1+=1
            a=a>>1
        while b>0:
            if b&1==1:
                s2+=1
            b=b>>1
        if s1>=s2:
            return s1*s2
        else:
            return s2//s1
                
        
        