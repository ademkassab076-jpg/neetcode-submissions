class Solution:
    def search(self, nums: List[int], target: int) -> int:  
        r=len(nums)-1
        l=0
        while r>=l:
            m=(l+r)//2
            if nums[m]<target:
                l=m+1
            elif nums[m]==target:
                return m
            else:
                r=m-1
        return -1