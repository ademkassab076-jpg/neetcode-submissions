from collections import Counter
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i=1
        test=False
        while not test:
            if i in nums:
                i+=1
            else:
                return i
        