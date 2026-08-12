class Solution(object):
    def findMaxLength(self, nums):
        balance = 0
        max_length = 0
        d = {0: -1}

        for i in range(len(nums)):
            if nums[i] == 0:
                balance -= 1
            else:
                balance += 1

            if balance in d:
                length = i - d[balance]
                max_length = max(max_length, length)
            else:
                d[balance] = i

        return max_length