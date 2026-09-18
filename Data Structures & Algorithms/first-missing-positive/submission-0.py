from collections import Counter
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i=1
        d=Counter(nums)
        test=False
        while not test:
            if i in d:
                i+=1
            else:
                return i
        