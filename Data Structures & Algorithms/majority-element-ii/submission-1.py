from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d=Counter(nums)
        lst=[]
        if d.most_common(2)[0][1]>(len(nums)//3):
            lst.append(d.most_common(2)[0][0])
        if d.most_common(2)[0][1]<len(nums) and d.most_common(2)[1][1]>(len(nums)//3):
            lst.append(d.most_common(2)[1][0])
        return lst