from typing import List


class Solution:

  def findAnagrams(self, s: str, p: str) -> List[int]:
    if len(p) > len(s):
      return []

    p_count = [0] * 26
    s_count = [0] * 26
    res = []

    for i in range(len(p)):
      p_count[ord(p[i]) - ord('a')] += 1
      s_count[ord(s[i]) - ord('a')] += 1

    if p_count == s_count:
      res.append(0)

    for i in range(len(p), len(s)):
      s_count[ord(s[i]) - ord('a')] += 1
      s_count[ord(s[i - len(p)]) - ord('a')] -= 1

      if p_count == s_count:
        res.append(i - len(p) + 1)

    return res
