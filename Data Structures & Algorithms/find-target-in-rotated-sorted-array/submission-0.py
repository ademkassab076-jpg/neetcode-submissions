class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        def binary_search(left,right):
            while left<=right:
                mid=(left+right)//2
                if nums[mid]>target:
                    right=mid-1
                elif nums[mid]==target:
                    return mid
                else:
                    left=mid+1
            return -1
        if nums[r]>=nums[l]:
            return binary_search(0,len(nums)-1)
        while True:
            m=(l+r)//2
            if nums[m]>nums[l]:
                l=m
            elif nums[m]<nums[l]:
                r=m
            else: 
                break 
        if target<nums[0]:
            return binary_search(m+1,len(nums)-1)
        return binary_search(0,m)
            