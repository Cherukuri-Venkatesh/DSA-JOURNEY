class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(s,n,p1,p2):
            while p1>=0 and p2<n and s[p1]==s[p2]:
                p1-=1
                p2+=1
            return s[p1+1:p2]
        n=len(s)
        ans=""
        if n==0:
            return ""
        for i in range(n):
            x=check(s,n,i-1,i+1)
            y=check(s,n,i,i+1)
            ans=max(ans,x,y,key=len)
        return ans
        