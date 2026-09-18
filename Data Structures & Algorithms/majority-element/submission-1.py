from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=Counter(nums)
        return d.most_common(1)[0][0]