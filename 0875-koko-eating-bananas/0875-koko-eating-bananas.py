class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l=1
        r=max(piles)
        while l<r:
            m=(l+r)//2
            hours=0
            for pile in piles:
                hours+=(pile+m-1)//m

            if hours<=h:
                r=m
            else:
                l=m+1
        return l
        