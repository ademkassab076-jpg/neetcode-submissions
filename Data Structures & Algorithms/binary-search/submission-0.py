class Solution:
    def search(self, nums: List[int], target: int) -> int:  
        l=len(nums)-1
        r=0
        while r<=l:
            m=(l+r)//2
            if nums[m]>target:
                l=m-1
            elif nums[m]==target:
                return m
            else:
                r=m+1
        return -1