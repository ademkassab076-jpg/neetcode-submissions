from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d=Counter(nums)
        lst=[]
        for key in d:
            if d[key]>len(nums)//3:
                lst.append(key)
        return lst