class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        nums.sort()
        nb=1
        a=1
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==1 and i==len(nums)-2 and nb+1>a:
                a=nb+1
            elif nums[i+1]-nums[i]==1:
                nb=nb+1
            elif nums[i+1]-nums[i]==0:
                continue
            elif nums[i+1]-nums[i]!=1  and nb>=a:
                a=nb
                nb=1
        return a if a!=1 else nb