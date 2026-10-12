class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        st=[0]*len(s)
        top=-1
        ans=""
        for word in s:
            top+=1
            st[top]=word
        while top!=-1:
            ans+=st[top]+" "
            top-=1
        return ans.strip()
            

        