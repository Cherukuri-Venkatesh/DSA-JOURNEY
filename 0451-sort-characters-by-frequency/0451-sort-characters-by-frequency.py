class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return ""
        min_as=ord(s[0])
        max_as=ord(s[0])
        for ch in s:
            ass=ord(ch)
            if ass < min_as:
                min_as=ass
            if ass>max_as:
                max_as=ass
        arr_s=max_as-min_as+1
        cnt=[0]*arr_s
        res=""
        for ch in s:
            cnt[ord(ch)-min_as]+=1
        for i in range(len(s),0,-1):
            freq=i
            for j in range(arr_s):
                if cnt[j]==freq:
                    for k in range(cnt[j]):
                        res+=chr(j+min_as)
        return res


