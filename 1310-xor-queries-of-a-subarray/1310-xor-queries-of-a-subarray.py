class Solution(object):
    def xorQueries(self, arr, queries):
        prefix = [0] * (len(arr) + 1)

        for i in range(len(arr)):
            prefix[i + 1] = prefix[i] ^ arr[i]

        result = []

        for left, right in queries:
            result.append(prefix[right + 1] ^ prefix[left])

        return result