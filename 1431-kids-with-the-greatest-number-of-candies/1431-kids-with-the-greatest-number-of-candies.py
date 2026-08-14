class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        arr=[]
        m=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies >=m:
                arr.append(True)
            else:
                arr.append(False)
        return arr
