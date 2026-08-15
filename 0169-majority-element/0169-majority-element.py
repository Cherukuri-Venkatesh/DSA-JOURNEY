from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=Counter(nums)
        max_count_num=count.most_common(1)[0][0]
        #max_count=count.most_common(1)[0][1]
        #max_count=max(count.values())
        return max_count_num

        