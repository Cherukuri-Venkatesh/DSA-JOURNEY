class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s=set(jewels)
        c=0
        for ch in stones:
            if ch in s:
                c+=1
        return c

        