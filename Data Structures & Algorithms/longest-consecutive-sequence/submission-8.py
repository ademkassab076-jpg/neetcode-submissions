class Solution:
    def longestConsecutive(self,nums):
        s = set(nums)
        best = 0
        for x in s:
            if x - 1 not in s:  
                length = 1
                while x + length in s:
                    length += 1
                best = max(best, length)
        return best