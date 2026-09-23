class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        l=0
        h=len(letters)-1
        while l<=h:
            m=(l+h)//2
            if letters[m]<=target:
                l=m+1
            else:
                h=m-1
        if l==len(letters):
            return letters[0]
        return letters[l]
        