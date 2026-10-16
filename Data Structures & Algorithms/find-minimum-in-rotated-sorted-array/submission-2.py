class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we're trying to get a O(log n) solution
        # it does mean that we re reducing the space where we are searching every time 
        #a binary search solution is for sure a good soltion but how?
        l,r=0,len(nums)-1
        if nums[l]<nums[r]:
            return nums[l]
        if l==r:
            return nums[0]
        while True:
            m=(l+r)//2
            if nums[m]>nums[l]:
                l=m
            elif nums[m]<nums[l]:
                r=m
            else:
                return nums[m+1]
        return 
        