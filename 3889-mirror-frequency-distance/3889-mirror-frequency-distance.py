class Solution:
    def mirrorFrequency(self, s: str) -> int:
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        visited=set()
        ans=0
        for ch in freq:
            if ch in visited:
                continue
                
            if ch.isdigit():
                mirror=chr(ord('0')+ord('9')-ord(ch))
            else:
                mirror=chr(ord('a')+ord('z')-ord(ch))
            ans+=abs(freq.get(ch,0)-freq.get(mirror,0))
            visited.add(ch)
            visited.add(mirror)
        return ans