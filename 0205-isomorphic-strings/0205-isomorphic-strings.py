class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        ss=set()
        tt=set()
        pairs=set()
        for i in range(len(s)):
            ss.add(s[i])
            tt.add(t[i])
            pairs.add((s[i],t[i]))
        if len(ss)==len(tt)==len(pairs):
            return True
        else:
            return False
        